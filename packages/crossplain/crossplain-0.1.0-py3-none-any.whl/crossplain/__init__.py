from itertools import product
from pathlib import Path
from typing import Callable
from dataclasses import dataclass
import crossplane
from rich import print

# def DirectiveNamed(name: str) -> Type[NamedTuple]:
#     return NamedTuple(name, line=int)
#
# class AbsoluteRedirect(DirectiveNamed("absolute_redirect")):
#     value: bool
#

global current_line
current_line = 0


@dataclass
class Directive:
    name: str
    args: list[str | int | bool]
    includes: list["ConfigurationFile"] | None = None
    block: list["Directive"] | None = None
    comment: str | None = None

    def json_ready(self) -> dict:
        global current_line
        current_line += 1
        d = {
            "directive": self.name,
            "line": current_line,
            "args": self.args,
        }
        if self.block is not None:
            d["block"] = [d.json_ready() for d in self.block]

        if self.name == "include":
            d["includes"] = self.includes or []

        if self.name == "#":
            d["comment"] = self.comment

        return d

    def __repr__(self) -> str:
        return f"{self.name} {' '.join(map(str, self.args))}" + (
            " { ... }" if self.block != None else ""
        )

    def walk(self, do: Callable[[int, "Directive"], None]):
        if self.block:
            for i, d in enumerate(self.block):
                do(i, d)
                d.walk(do)


@dataclass
class Server(Directive):
    def __init__(self, _directive=None, **kwargs):
        super().__init__(**kwargs)
        self._directive = _directive

    @property
    def locations(self) -> list[Directive]:
        return [l for l in self.block if l.name == "location"]

    @locations.setter
    def locations(self, locations: list[Directive]):
        new_block = []
        current_location_directive_index = 0
        for directive in self.block:
            if directive.name == "location" and current_location_directive_index < len(
                locations
            ):
                new_block.append(locations[current_location_directive_index])
                current_location_directive_index += 1
            else:
                new_block.append(directive)
        self.block = new_block
        self._directive.block = self.block



@dataclass
class ConfigurationFile:
    filepath: Path
    directives: list[Directive]

    def dict(self) -> dict:
        return {
            "file": str(self.filepath),
            "status": "ok",
            "errors": [],
            "parsed": [d.json_ready() for d in self.directives],
        }

    def build(self) -> str:
        return crossplane.build(self.dict()["parsed"])

    def server(self, name: str, port: int) -> Server:
        for i, d in enumerate(self.directives):
            if (
                d.name == "server"
                and name == [s.args[0] for s in d.block if s.name == "server_name"][0]
                and str(port) == [s.args[0] for s in d.block if s.name == "listen"][0]
            ):
                return Server(
                    _directive=d,
                    name="server",
                    args=d.args,
                    block=d.block,
                )
        raise KeyError(f"No server with server_name {name!r} and port {port!r}")

    def walk(self, do: Callable[[int, Directive], None]):
        for i, d in enumerate(self.directives):
            do(i, d)
            d.walk(do)


@dataclass
class NGINXConfiguration:
    files: list[ConfigurationFile]

    def build(self) -> dict[str, str]:
        return {
            f.filepath: str(crossplane.build(f.dict()["parsed"])) for f in self.files
        }

    def __getitem__(self, __name: str) -> ConfigurationFile:
        if (
            len(
                matches := [
                    f
                    for f in self.files
                    if __name in {str(f.filepath), f.filepath.name}
                ]
            )
            > 0
        ):
            return matches[0]
        raise AttributeError(f"No such file: {__name}. Available files: {self.files}")


def _parse(filepath: str | Path, combine: bool = False) -> list[ConfigurationFile]:
    response = crossplane.parse(str(filepath), combine=combine, comments=True)
    if response["status"] == "failed":
        raise Exception(
            f"The following errors occured while parsing {filepath}: \n"
            + "\n".join(
                f"· {e['file']}:{e['line']} {e['error']}" for e in response["errors"]
            )
        )

    return [
        ConfigurationFile(
            filepath=Path(file["file"]),
            directives=list(map(_instanciate_directive, file["parsed"])),
        )
        for file in response["config"]
    ]


def parse(filepath: str | Path) -> NGINXConfiguration:
    return NGINXConfiguration(_parse(filepath, combine=False))


def parse_combined(filepath: str | Path) -> ConfigurationFile:
    return _parse(filepath, combine=True)[0]


def _instanciate_directive(directive: dict) -> Directive:
    d = Directive(
        name=directive["directive"],
        args=directive["args"],
        block=None,
        includes=directive.get("includes"),
        comment=directive.get("comment"),
    )
    if directive.get("block"):
        d.block = list(map(_instanciate_directive, directive["block"]))

    return d


if __name__ == "__main__":
    p = parse(Path(__file__).parent / ".." / "in" / "nginx.conf")["local.conf"]

    for name, port in product(
        ("fr.ewen.works", "en.ewen.works", "ewen.works", "schoolsyst.com"), (80, 443)
    ):
        server = p.server(name, port)
        server.block += [error_page(404, "404.html"), error_page(500, "500.html")]
        server.locations = [
            location("/", try_files("$uri", "$uri.html", "$uri/", "=404"))
        ] + server.locations

    for name, port in product(("assets.ewen.works", "media.ewen.works"), (443, 80)):
        server = p.server(name, port)
        server.block += [
            add_header("Access-Control-Allow-Origin", "*"),
            location(
                "/",
                autoindex(),
                autoindex_format("xml"),
                xslt_stylesheet("/home/user-data/www/superbindex.xslt"),
                types(
                    {
                        "text/plain": [
                            "indentex",
                            "tex",
                            "txt",
                            "json",
                            "yaml",
                            "yml",
                            "toml",
                        ]
                    }
                ),
            ),
        ]

    p.server("ewen.works", 443).locations = [
        location(
            "/",
            _if(
                "$http_accept_language ~* ^fr",
                _return(301, "https://fr.ewen.works$request_uri"),
            ),
            _return(301, "https://en.ewen.works$request_uri"),
        )
    ]

    (Path(__file__).parent / "example" / "out" / "local.conf").write_text(p.build())

    input()

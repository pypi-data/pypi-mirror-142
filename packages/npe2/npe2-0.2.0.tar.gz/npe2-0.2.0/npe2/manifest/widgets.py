from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Optional

from pydantic import BaseModel, Extra, Field

from ..types import Widget
from .utils import Executable

if TYPE_CHECKING:
    from .._command_registry import CommandRegistry


class WidgetContribution(BaseModel, Executable[Widget]):
    """Contribute a widget that can be added to the napari viewer.

    Widget contributions point to a **command** that, when called, returns a widget
    *instance*; this includes functions that return a widget instance, (e.g. those
    decorated with `magicgui.magic_factory`) and subclasses of either
    [`QtWidgets.QWidget`](https://doc.qt.io/qt-5/qwidget.html) or
    [`magicgui.widgets.Widget`](https://napari.org/magicgui/api/_autosummary/magicgui.widgets._bases.Widget.html).

    Optionally, **autogenerate** may be used to create a widget (using
    [magicgui](https://napari.org/magicgui/)) from a command.  (In this case, the
    command needn't return a widget instance; it can be any function suitable as an
    argument to `magicgui.magicgui()`.)
    """

    command: str = Field(
        ...,
        description="Identifier of a command that returns a widget instance.  "
        "Or, if `autogenerate` is `True`, any command suitable as an argument "
        "to `magicgui.magicgui()`.",
    )
    display_name: str = Field(
        ..., description="Name for the widget, as presented in the UI."
    )
    autogenerate: bool = Field(
        default=False,
        description="If true, a widget will be autogenerated from the signature of "
        "the associated command using [magicgui](https://napari.org/magicgui/).",
    )

    class Config:
        extra = Extra.forbid

    def get_callable(
        self, _registry: Optional[CommandRegistry] = None
    ) -> Callable[..., Widget]:
        func = super().get_callable()
        if self.autogenerate:
            from magicgui import magic_factory

            return magic_factory(func)
        return func

# -*- coding: utf-8 -*-
from aitoolkit import _
from aitoolkit.interfaces import IAitoolkitLayer
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IControlPanel(Interface):
    """Control Panel schema for AI Toolkit settings."""

    summarisation = schema.Bool(
        title=_("Enable summarisation"),
        description=_("[WIP] Enable or disable summarisation"),
        default=False,
        required=False,
        readonly=False,
    )
    recommendations = schema.Bool(
        title=_("Enable recommendations"),
        description=_("[WIP] Enable or disable recommendations"),
        default=False,
        required=False,
        readonly=False,
    )
    content_performance = schema.Bool(
        title=_("Enable content performance"),
        description=_("[WIP] Enable or disable content performance"),
        default=False,
        required=False,
        readonly=False,
    )
    seo = schema.Bool(
        title=_("Enable SEO"),
        description=_("[WIP] Enable or disable SEO"),
        default=False,
        required=False,
        readonly=False,
    )
    chatbot = schema.Bool(
        title=_("Enable chatbot"),
        description=_("[WIP] Enable or disable chatbot"),
        default=False,
        required=False,
        readonly=False,
    )
    llm= schema.Choice(
        title=_("Select LLM"),
        description=_("Select the LLM to use"),
        values=["gpt-3.5-turbo", "gpt-4"],
        default="gpt-3.5-turbo",
    )
    api_key = schema.TextLine(
        title=_(
            "Enter API Key",
        ),
        description=_(
            "Only required if you are using third-party LLMs.",
        ),
        default="",
        required=False,
        readonly=False,
    )

class ControlPanel(RegistryEditForm):
    schema = IControlPanel
    schema_prefix = "aitoolkit.control_panel"
    label = _("AI Toolkit Settings")


ControlPanelView = layout.wrap_form(ControlPanel, ControlPanelFormWrapper)


@adapter(Interface, IAitoolkitLayer)
class ControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IControlPanel
    configlet_id = "control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("AI Toolkit Settings")
    group = ""
    schema_prefix = "aitoolkit.control_panel"

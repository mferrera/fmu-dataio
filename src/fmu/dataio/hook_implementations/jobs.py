try:
    from ert.shared.plugins.plugin_manager import hook_implementation
    from ert.shared.plugins.plugin_response import plugin_response
except ModuleNotFoundError:
    from ert_shared.plugins.plugin_manager import hook_implementation
    from ert_shared.plugins.plugin_response import plugin_response


@hook_implementation
@plugin_response(plugin_name="fmu_dataio")
def installable_workflow_jobs():
    return {}

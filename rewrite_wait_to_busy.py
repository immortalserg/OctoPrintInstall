# coding=utf-8
 
import logging
 
def rewrite_wait_to_busy(comm_instance, line, *args, **kwargs):
    if line == "wait" or line.startswith("wait"):
        return "echo:busy processing"
    else:
        return line
 
__plugin_name__ = "Rewrite wait to busy"
__plugin_description__ = "Rewrites received wait responses to echo:busy processing for broken firmware misunderstanding when wait should be used"
__plugin_author__ = "Gina Häußge"
__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.received": rewrite_wait_to_busy
}

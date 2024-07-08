def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

colors = {
    "labelColor" : _from_rgb((211, 211, 211)),
    "popColor" : _from_rgb((131, 135, 138)),
    "actionColor" : _from_rgb((120, 183, 235)),
    "numberColor" : _from_rgb((120, 235, 171)),
    "rootColor" : _from_rgb((130, 120, 130))
}
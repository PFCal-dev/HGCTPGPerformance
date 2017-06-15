import rootpy.ROOT as ROOT
from rootpy.context import preserve_current_canvas
from rootpy.memory import keepalive


def HGCAL_label(text='HGCAL Simulation', pad=None):
    """Add label to the current Pad."""
    if pad is None:
        pad = ROOT.gPad.func()
    with preserve_current_canvas():
        pad.cd()
        left_margin = pad.GetLeftMargin()
        top_margin = pad.GetTopMargin()
        # Offset labels by 14% of the top margin
        ypos = 1 - 0.86*top_margin 
        label_cms = ROOT.TLatex(left_margin, ypos, "CMS")
        label_cms.SetTextFont(61) # Helvetica bold
        label_cms.SetTextAlign(11) # left-bottom
        label_cms.SetNDC()
        # The text is 75% as tall as the margin it lives in.
        label_cms.SetTextSize(0.75 * top_margin)
        label_cms.Draw()
        keepalive(pad, label_cms)
        # Draw additional text if desired
        label_add = None
        if text:
            label_add = ROOT.TLatex(left_margin+0.09, ypos, text)
            label_add.SetTextFont(52) # Helvetica italic
            label_add.SetTextAlign(11) # left-bottom
            label_add.SetNDC()
            # The text is 75% as tall as the margin it lives in.
            label_add.SetTextSize(0.60 * top_margin)
            label_add.Draw()
            keepalive(pad, label_add)
        pad.Modified()
        pad.Update()
    return label_cms, label_add

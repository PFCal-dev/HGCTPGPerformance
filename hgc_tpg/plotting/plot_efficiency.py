import attr
from attr.validators import instance_of
import rootpy.ROOT as ROOT
from rootpy.plotting import Canvas, Hist2D
import numpy as np
from hgc_tpg.plotting.labels import HGCAL_label

@attr.s
class Parameters(object):
    '''Class encapsulating plot parameters/config.'''
    name = attr.ib(validator=instance_of(str), default='efficiency')
    # Axis
    xmin = attr.ib(validator=instance_of(float), default=0.)
    xmax = attr.ib(validator=instance_of(float), default=50.)
    ymin = attr.ib(validator=instance_of(float), default=0.)
    ymax = attr.ib(validator=instance_of(float), default=1.1)
    xtitle = attr.ib(validator=instance_of(str), default='p_{T}^{gen}')
    ytitle = attr.ib(validator=instance_of(str), default='Efficiency')
    # Graph
    efficiency_markerstyle = attr.ib(default='square')
    efficiency_markersize = attr.ib(validator=instance_of(float), default=1.)
    efficiency_markercolor = attr.ib(default=ROOT.kBlack)
    # Legend 
    legend_x1 = attr.ib(validator=instance_of(float), default=0.68)
    legend_y1 = attr.ib(validator=instance_of(float), default=0.76)
    legend_x2 = attr.ib(validator=instance_of(float), default=0.68)
    legend_y2 = attr.ib(validator=instance_of(float), default=0.76)
    legendtext_size = attr.ib(validator=instance_of(float), default=0.035)
    legendtext_font = attr.ib(validator=instance_of(int), default=42)


def draw_axes(params):
    '''Draw axes of the plot'''
    dummy_histo = Hist2D(1, params.xmin, params.xmax, 1, params.ymin, params.ymax)
    dummy_histo.xaxis.SetTitle(params.xtitle)
    dummy_histo.yaxis.SetTitle(params.ytitle)
    dummy_histo.Draw()
    return dummy_histo


def draw_efficiency(params, efficiency):
    ''' Draw 68% and 95% contours'''
    efficiency.markerstyle = params.efficiency_markerstyle
    efficiency.markersize = params.efficiency_markersize
    efficiency.efficiency_markercolor = params.efficiency_markercolor
    efficiency.Draw('p')

def draw_lines(params):
    lines = []
    line_100 = ROOT.TLine(params.xmin, 1, params.xmax, 1)
    line_95 = ROOT.TLine(params.xmin, 0.95, params.xmax, 0.95)
    line_100.SetLineWidth(2)
    line_95.SetLineWidth(2)
    line_95.SetLineStyle(2)
    line_100.Draw()
    line_95.Draw()
    lines.append(line_100)
    lines.append(line_95)
    return lines 


def draw_legends(params):
    return

def plot(params, efficiency):
    canvas = Canvas(width=500, height=500)
    draw_axes(params)
    draw_efficiency(params, efficiency)
    draw_lines(params)
    HGCAL_label(text='HGCAL Simulation',
            pad=canvas)
    draw_legends(params)
    canvas.RedrawAxis()
    canvas.Print('%s.png'%params.name)
    canvas.Print('%s.pdf'%params.name)
    canvas.Print('%s.C'%params.name)

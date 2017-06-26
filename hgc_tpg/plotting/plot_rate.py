import attr
from attr.validators import instance_of
import rootpy.ROOT as ROOT
from rootpy.plotting import Canvas, Hist2D
import numpy as np
from hgc_tpg.plotting.labels import HGCAL_label

@attr.s
class Parameters(object):
    '''Class encapsulating plot parameters/config.'''
    name = attr.ib(validator=instance_of(str), default='rate')
    # Axis
    xmin = attr.ib(validator=instance_of(float), default=0.)
    xmax = attr.ib(validator=instance_of(float), default=50.)
    ymin = attr.ib(validator=instance_of(float), default=0.)
    ymax = attr.ib(validator=instance_of(float), default=1.1)
    xtitle = attr.ib(validator=instance_of(str), default='Threshold [GeV]')
    ytitle = attr.ib(validator=instance_of(str), default='Rate [kHz]')
    # Graph
    fill_color = attr.ib(default=ROOT.kBlack)
    fill_style = attr.ib(default='solid')


def draw_axes(params):
    '''Draw axes of the plot'''
    dummy_histo = Hist2D(1, params.xmin, params.xmax, 1, params.ymin, params.ymax)
    dummy_histo.xaxis.SetTitle(params.xtitle)
    dummy_histo.yaxis.SetTitle(params.ytitle)
    dummy_histo.Draw()
    return dummy_histo


def draw_rates(params, rate):
    rate.fillcolor = params.fill_color
    rate.fillstyle = params.fill_style
    rate.Draw('l3')



def plot(params, rates):
    canvas = Canvas(width=500, height=500)
    draw_axes(params)
    draw_rates(params, rates)
    HGCAL_label(text='HGCAL Simulation',
            pad=canvas)
    canvas.SetLogy()
    canvas.RedrawAxis()
    canvas.Print('%s.png'%params.name)
    canvas.Print('%s.pdf'%params.name)
    canvas.Print('%s.C'%params.name)

from numpy import random as r
from bokeh.client import push_session
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import CrosshairTool,HoverTool
from bokeh.embed import autoload_server as s
x=[1]
y=[r.randint(50)]

p = figure(x_range=(0,11),plot_width=750,plot_height=300)
p.add_tools(CrosshairTool())
p.add_tools(HoverTool())
r = p.line(x,y,line_width=2)
curdoc().title='live'
#session = push_session(curdoc())
#script=s(p,session_id=session.id)
#print(script)
ds = r.data_source
y=0

def update():
    global y
    from numpy import random as r
    a=ds.data['x']+[ds.data['x'][-1]+1]
    c=r.randint(50)
    b=ds.data['y']+[c]
    ds.data.update(x=a,y=b)
    y=y+1
    if(y>20):
        p.x_range.start+=1
        p.x_range.end+=1

curdoc().add_root(p)
curdoc().add_periodic_callback(update,2000)

#session.show(p)

#session.loop_until_closed()


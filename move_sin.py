
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax=plt.subplots()

x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))

def init():
    line.set_ydata([np.nan]*len(x))
    return line,

def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line,

ani =animation.FuncAnimation(fig,animate,inti_func=init,interval=5,blit=True,save_count=50)
ani.save('animation.gif',writer='pillow')
plt.show()


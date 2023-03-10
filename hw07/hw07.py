#!/usr/bin/python3
import json
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as inte

def data(cal, imu, out):
    f=open(cal)
    cal=json.load(f)
    f.close()
    
    #using pandas to create an empty array at 'loc,col,value'
    
    df=pd.read_csv("../test/{}.csv".format(imu))
    df.insert(2, "v_x", np.zeros(4000))
    df.insert(3, "v_y", np.zeros(4000))
    df.insert(4, "v_z", np.zeros(4000))
    
    #filling arrays with integrated values to get mps and rps
    df['v_x'][1:]=inte.cumtrapz((df['a_x']*cal['a_x_scale']), df['time'], dx=1.0, axis=-1, initial=None)
    df['v_y'][1:]=inte.cumtrapz((df['a_y']*cal['a_y_scale']), df['time'], dx=1.0, axis=-1, initial=None)
    df['v_z'][1:]=inte.cumtrapz((df['a_z']*cal['a_z_scale']), df['time'], dx=1.0, axis=-1, initial=None)

    #same as before, creating empty arrays
    df.insert(5, "x", np.zeros(4000))
    df.insert(6, "y", np.zeros(4000))
    df.insert(7, "z", np.zeros(4000))
    
    #integrate again for y values of mps andrps
    df['x'][1:]= inte.cumtrapz(df['v_x'], df['time'], dx=1.0, axis=-1, initial=None)
    df['y'][1:]= inte.cumtrapz(df['v_y'], df['time'], dx=1.0, axis=-1, initial=None)
    df['z'][1:]= inte.cumtrapz(df['v_z'], df['time'], dx=1.0, axis=-1, initial=None)
    
    #plotting data
    fig, axs = plt.subplots(3)
    fig.set_figheight(9)
    fig.set_figwidth(8)

    axs[0].set_ylabel("Position [m]")
    axs[0].set_title("Linear")
    df.plot(x='time', y=['x','y','z'] ,ax=axs[0])
    axs[1].set_ylabel("Velocity [m/s]")
    df.plot(x='time', y=['v_x','v_y','v_z'], ax=axs[1])
    axs[2].set_ylabel("Accel [m/s^2]")
    df.plot(x='time', y=['a_x','a_y','a_z'], ax=axs[2])

    #save fig
    plt.savefig('{}_linear.png'.format(imu))
    
    #calculating roll,pitch,yaw and creating empty array
    df.insert(11, "roll", np.zeros(4000))
    df.insert(12, "pitch", np.zeros(4000))
    df.insert(13, "yaw", np.zeros(4000))
    
    #mps and rps
    df['roll'][1:]=inte.cumtrapz((df['v_roll']*cal['v_roll_scale']), df['time'], dx=1.0, axis=-1, initial=None)
    df['pitch'][1:]=inte.cumtrapz((df['v_pitch']*cal['v_pitch_scale']), df['time'], dx=1.0, axis=-1, initial=None)
    df['yaw'][1:]=inte.cumtrapz((df['v_yaw']*cal['v_yaw_scale']), df['time'], dx=1.0, axis=-1, initial=None)

    df.insert(17, "a_roll", np.zeros(4000))
    df.insert(18, "a_pitch", np.zeros(4000))
    df.insert(19, "a_yaw", np.zeros(4000))
    
    #partial vroll/partial time
    df['a_roll']=df['v_roll'].diff()/df['time'].diff()
    df['a_pitch']=df['v_pitch'].diff()/df['time'].diff()
    df['a_yaw']=df['v_yaw'].diff()/df['time'].diff()

    #plotting and saving fig
    fig, axs = plt.subplots(3)
    fig.set_figheight(9)
    fig.set_figwidth(8)
    axs[0].set_ylabel("Position [rad]")
    axs[0].set_title("Angular")
    df.plot(x='time', y=['roll','pitch','yaw'] ,ax=axs[0])
    axs[1].set_ylabel("Velocity [rad/s]")
    df.plot(x='time', y=['v_roll','v_pitch','v_yaw'], ax=axs[1])
    axs[2].set_ylabel("Accel [rad/s^2]")
    df.plot(x='time', y=['a_roll','a_pitch','a_yaw'], ax=axs[2])

    plt.savefig('{}_angular.png'.format(imu))
    plt.show()
    df.to_csv(out,index=False, float_format='%.6e')


def main():
    #makes sure length is long enough
    
    l=len(sys.argv)
    if l == 4:
        cal=sys.argv[1]
        imu=os.path.splitext(os.path.basename(sys.argv[2]))[0]
        out=sys.argv[3]
        data(cal,imu,out)
    else:
        print("3 Arguments required, .json .csv .csv")
        sys.exit(1)


if __name__ == '__main__':
    main()

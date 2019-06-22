import vrep
import keyboard
import time
import sys, math     
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
   
vrep.simxFinish(-1)
 
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV = 360
n=1
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
     
errorCode,Sphere_handle=vrep.simxGetObjectHandle(clientID,'Sphere',vrep.simx_opmode_oneshot_wait)
errorCode,P1_handle=vrep.simxGetObjectHandle(clientID,'P1',vrep.simx_opmode_oneshot_wait)
errorCode,R1_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
errorCode,R2_handle=vrep.simxGetObjectHandle(clientID,'R2',vrep.simx_opmode_oneshot_wait)
errorCode,R3_handle=vrep.simxGetObjectHandle(clientID,'R3',vrep.simx_opmode_oneshot_wait)
errorCode,R4_handle=vrep.simxGetObjectHandle(clientID,'R4',vrep.simx_opmode_oneshot_wait)
 
 
vrep.simxSetJointTargetVelocity(clientID,P1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R2_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R3_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R4_handle,0,vrep.simx_opmode_oneshot_wait)
 
 
def con(): 
      errorCode = vrep.simxSetJointTargetVelocity(clientID,R1_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
def clo():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,R1_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait) 
def right():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,P1_handle,2,vrep.simx_opmode_oneshot_wait)
def left():
      errorCode =  vrep.simxSetJointTargetVelocity(clientID,P1_handle,-200,vrep.simx_opmode_oneshot_wait)
def con1():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,R2_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
def clo1():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,R2_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait) 
def con2():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,R3_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
def clo2():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,R3_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait) 
def con3():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,R4_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
def clo3():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,R4_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait) 
 
 
vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
while True:
    try:
            if keyboard.is_pressed('a'): 
                con()
            else:  
                clo()
            if keyboard.is_pressed('Up Arrow'):  
                right()
            else:  
                left()

            if keyboard.is_pressed('l'): 
                clo1()
            else:  
                con1()

            if keyboard.is_pressed('a'): 
                con2()
            else:  
                clo2()
            if keyboard.is_pressed('l'): 
                clo3()
            else:  
                con3()

    except:
            break
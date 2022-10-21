from module import move_motor as stepmotor



# setting motor parameter
wait = 0.001
step = 1
deg = step * 4096
IN1 = 2              # blue to blue
IN2 = 3              # pink to red
IN3 = 4              # yellow to yellow
IN4 = 17             # orange to black
motor = stepmotor.C28BYJ48(IN1, IN2, IN3, IN4)



if __name__ == '__main__':
    while True:
        # Select step
        print('Select_step')
        step = float(input())
        deg = step * 4096

        if step > 0:
            motor.Step_CW(deg, wait)
        elif step < 0:
            motor.Step_CCW(deg, wait)
        else:
            break

    motor.Cleanup()
    print('finish')
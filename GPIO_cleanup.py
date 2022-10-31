from module import move_motor as stepmotor


IN1 = 2              # blue to blue
IN2 = 3              # pink to red
IN3 = 4              # yellow to yellow
IN4 = 17             # orange to black
motor = stepmotor.C28BYJ48(IN1, IN2, IN3, IN4)
motor.Cleanup()

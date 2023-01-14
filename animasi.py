from drawingpanel import *


def pose1(x, y, color="black"):
    # KEPALA
    panel.canvas.create_oval(abs(x + 10), y + 50, abs(x + 40), y + 80, fill=color, outline=color)

    # BADAN
    panel.canvas.create_line(abs(x + 25), y + 55, abs(x + 25), y + 130, fill=color, width=10)

    # TANGAN KIRI
    panel.canvas.create_line(abs(x + 10), y + 125, abs(x + 25), abs(y + 80), fill=color, width=10)

    # TANGAN KANAN
    panel.canvas.create_line(abs(x + 40), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # KAKI KIRI
    panel.canvas.create_line(abs(x + 15), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x), y + 170, abs(x + 15), y + 155, fill=color, width=10)

    # KAKI KANAN
    panel.canvas.create_line(abs(x + 40), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 40), y + 175, abs(x + 40), y + 155, fill=color, width=10)


def pose2(x, y, color="black"):
    # KEPALA
    panel.canvas.create_oval(abs(x + 10), y + 50, abs(x + 40), y + 80, fill=color, outline=color)

    # BADAN
    panel.canvas.create_line(abs(x + 25), y + 55, abs(x + 25), y + 130, fill=color, width=10)

    # TANGAN KIRI
    panel.canvas.create_line(abs(x + 10), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # TANGAN KANAN
    panel.canvas.create_line(abs(x + 40), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # KAKI KIRI
    panel.canvas.create_line(abs(x + 20), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 15), y + 175, abs(x + 20), y + 155, fill=color, width=10)

    # KAKI KANAN
    panel.canvas.create_line(abs(x + 35), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 40), y + 175, abs(x + 35), y + 155, fill=color, width=10)


def pose3(x, y, color="black"):
    # KEPALA
    panel.canvas.create_oval(abs(x + 10), y + 50, abs(x + 40), y + 80, fill=color, outline=color)

    # BADAN
    panel.canvas.create_line(abs(x + 25), y + 55, abs(x + 25), y + 130, fill=color, width=10)

    # TANGAN KIRI
    panel.canvas.create_line(abs(x + 10), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # TANGAN KANAN
    panel.canvas.create_line(abs(x + 40), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # KAKI KIRI
    panel.canvas.create_line(abs(x + 35), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 40), y + 175, abs(x + 35), y + 155, fill=color, width=10)

    # KAKI KANAN
    panel.canvas.create_line(abs(x + 25), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 10), y + 175, abs(x + 25), y + 155, fill=color, width=10)


def pose4(x, y, color="black"):
    # KEPALA
    panel.canvas.create_oval(abs(x + 10), y + 50, abs(x + 40), y + 80, fill=color, outline=color)

    # BADAN
    panel.canvas.create_line(abs(x + 25), y + 55, abs(x + 25), y + 130, fill=color, width=10)

    # TANGAN KIRI
    panel.canvas.create_line(abs(x + 10), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # TANGAN KANAN
    panel.canvas.create_line(abs(x + 40), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # KAKI KIRI
    panel.canvas.create_line(abs(x + 35), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 35), y + 175, abs(x + 35), y + 155, fill=color, width=10)

    # KAKI KANAN
    panel.canvas.create_line(abs(x + 15), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 5), y + 175, abs(x + 15), y + 155, fill=color, width=10)


def pose5(x, y, color="black"):
    # KEPALA
    panel.canvas.create_oval(abs(x + 10), y + 50, abs(x + 40), y + 80, fill=color, outline=color)

    # BADAN
    panel.canvas.create_line(abs(x + 25), y + 55, abs(x + 25), y + 130, fill=color, width=10)

    # TANGAN KIRI
    panel.canvas.create_line(abs(x + 10), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # TANGAN KANAN
    panel.canvas.create_line(abs(x + 40), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # KAKI KIRI
    panel.canvas.create_line(abs(x + 35), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 40), y + 175, abs(x + 35), y + 155, fill=color, width=10)

    # KAKI KANAN
    panel.canvas.create_line(abs(x + 25), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 10), y + 175, abs(x + 25), y + 155, fill=color, width=10)


def pose6(x, y, color="black"):
    # KEPALA
    panel.canvas.create_oval(abs(x + 10), y + 50, abs(x + 40), y + 80, fill=color, outline=color)

    # BADAN
    panel.canvas.create_line(abs(x + 25), y + 55, abs(x + 25), y + 130, fill=color, width=10)

    # TANGAN KIRI
    panel.canvas.create_line(abs(x + 10), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # TANGAN KANAN
    panel.canvas.create_line(abs(x + 40), y + 125, abs(x + 25), y + 80, fill=color, width=10)

    # KAKI KIRI
    panel.canvas.create_line(abs(x + 20), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 15), y + 175, abs(x + 20), y + 155, fill=color, width=10)

    # KAKI KANAN
    panel.canvas.create_line(abs(x + 35), y + 155, abs(x + 25), y + 130, fill=color, width=10)
    panel.canvas.create_line(abs(x + 40), y + 175, abs(x + 35), y + 155, fill=color, width=10)

def Reverse_Pose(Pose):
    pass

if __name__ == "__main__":
    panel = DrawingPanel(500, 300)
    panel.set_background("white")
    delay = 2000
    while True:
        # First Pose
        panel.clear()
        pose1(10, 30)
        panel.sleep(delay)
        panel.clear()
        # Second Pose
        pose2(60, 30)
        panel.sleep(delay)
        panel.clear()
        # Third Pose
        pose3(110, 30)
        panel.sleep(delay)
        panel.clear()
        # Fourth Pose
        pose4(160, 30)
        panel.sleep(delay)
        panel.clear()
        # Fifth Pose
        pose5(210, 30)
        panel.sleep(delay)
        panel.clear()
        # Final Pose
        pose6(260, 30)
        panel.clear()
        #Walking to the left
        pose1(-260, 30)
        panel.sleep(delay)
        panel.clear()
        pose2(-210, 30)
        panel.sleep(delay)
        panel.clear()
        pose3(-160, 30)
        panel.sleep(delay)
        panel.clear()
        pose4(-110, 30)
        panel.sleep(delay)
        panel.clear()
        pose5(-60, 30)
        panel.sleep(delay)
        panel.clear()
        pose6(-10, 30)
        panel.clear()


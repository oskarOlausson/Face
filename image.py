import numpy

class Image():

    def __init__(self,path):
        f = open(path)
        self.img = f.readlines()
        self.current_line = 0
        self.currentImage = self.parse_next_image()
        f.close()

    def reset_current_line(self):
        self.current_line = 0

    def find_next_image(self):
        stop = False
        while(not stop):
            line = self.img[self.current_line]
            stop = (line.find("Image")==0)
            self.next_line()
            if stop: return self.current_line

    def parse_next_image(self):
        self.find_next_image()
        return self.parse_image()

    def parse_image_line(self):
        line = self.img[self.current_line].split()
        line = [int(x) for x in line if x != " "]
        return line

    def next_line(self):
        self.current_line += 1
        return self.current_line

    def parse_image(self):
        image = list()
        for i in range(0,20):
            image.append(self.parse_image_line())
            self.next_line()
        return image

    def check_pixel(self,x,y):
        return self.currentImage[y][x]



if __name__ == "__main__":

    img = Image('./material/training-A.txt')
    img.parse_next_image()
    print(img.check_pixel(1,1))












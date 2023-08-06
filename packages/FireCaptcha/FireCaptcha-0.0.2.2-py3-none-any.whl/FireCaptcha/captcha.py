import os
import io
import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter


FONTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'fonts')
DEFAULT_FONT = os.path.join(FONTS_DIR, 'Monaco.ttf')


class FinishedCaptcha():
    def __init__(self, image, answer):
        self.image = image
        self.answer = answer


class ImageCaptcha:
    def __init__(self,
                width: int = 300,
                height: int = 100,
                char_number: int = 4,
                char_color: str = '#3ee6f9',
                char_type: int = 1,
                bg_color: str = '#343232',
                gradient: str = '',
                misleading_lines: int = 0,
                misleading_dots: int = 0,
                misleading_color: str = '#e6cd79'):
        self.width = width
        self.height = height
        self.char_number = char_number
        self.char_color = char_color
        self.char_type = char_type
        self.bg_color = bg_color
        self.gradient = gradient
        self.misleading_lines = misleading_lines
        self.misleading_dots = misleading_dots
        self.misleading_color = misleading_color

        if self.bg_color.lower() == 'random':
            self.bg_color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        if self.gradient.lower() == 'random':
            self.gradient = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

        self.image = None
        self.answer = None

    def generate_gradient(
        self, colour1: str, colour2: str, width: int, height: int) -> Image:
        """Generate a vertical gradient."""
        base = Image.new('RGB', (width, height), colour1)
        top = Image.new('RGB', (width, height), colour2)
        mask = Image.new('L', (width, height))
        mask_data = []
        for y in range(height):
            mask_data.extend([int(255 * (y / height))] * width)
        mask.putdata(mask_data)
        base.paste(top, (0, 0), mask)
        return base


    def generate_position(self, i, font_size):
        offset_x = int(self.width / self.char_number * 0.4)
        offset_y = font_size

        space_for_char = self.width / self.char_number

        x_min = space_for_char * i + offset_x
        x_max = space_for_char * (i + 1) - offset_x

        y_min = 0
        y_max = self.height - offset_y * 1.2

        x = random.randint(int(x_min), int(x_max))
        y = random.randint(int(y_min), int(y_max))

        return x, y

    def draw_chars(self, chars, image):
        answer = ''
        for i in range(self.char_number):
            char = random.choice(chars)

            answer += char

            font_size = random.randint(self.height * 0.3, self.height * 0.4)

            x, y = ImageCaptcha.generate_position(self, i, font_size)


            font = ImageFont.truetype('arial', font_size)
            #draw char
            draw = ImageDraw.Draw(image)

            if self.char_color.lower() == 'random':
                #generate random hex color
                color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

                draw.text((x, y), char, color, font)
            else:
                draw.text((x, y), char, self.char_color, font)

        return answer

    def draw_misleading_lines(self, image):
        if self.misleading_lines <= 0:
            return
        draw = ImageDraw.Draw(image)
        for _ in range(self.misleading_lines):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)

            if self.misleading_color.lower() == 'random':
                color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
                draw.line((x1, y1, x2, y2), fill=color, width=4)
            else:
                draw.line((x1, y1, x2, y2), fill=self.misleading_color, width=4)

    def draw_misleading_dots(self, image):
        if self.misleading_dots <= 0:
            return
        draw = ImageDraw.Draw(image)
        for _ in range(self.misleading_dots):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            radius = random.randint(0, self.width / 30)

            if self.misleading_color.lower() == 'random':
                color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
                draw.ellipse((x, y, x + radius, y + radius), fill=color)
            else:
                draw.ellipse((x, y, x + radius, y + radius), fill=self.misleading_color)


    def Generate(self) -> FinishedCaptcha:
        if self.gradient:
            image = self.generate_gradient(
                self.gradient, self.bg_color, self.width, self.height)
        else:
            image = Image.new('RGB', (self.width, self.height), self.bg_color)

        if self.char_type == 1:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        elif self.char_type == 2:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXY'
        elif self.char_type == 3:
            chars = 'abcdefghijklmnopqrstuvwxyz'
        elif self.char_type == 4:
            chars = '0123456789'

        answer = ImageCaptcha.draw_chars(self, chars, image)

        ImageCaptcha.draw_misleading_lines(self, image)

        ImageCaptcha.draw_misleading_dots(self, image)

        return FinishedCaptcha(image, answer)

class GifCaptcha():
    def __init__(self,
                width: int = 300,
                height: int = 100,
                char_number: int = 4,
                char_color: str = '#3ee6f9',
                char_type: int = 1,
                frame_delay: int = 2000,
                bg_color: str = '#343232',
                gradient: str = '',
                start_text: str = 'Start',
                end_text: str = 'End',):
        self.width = width
        self.height = height
        self.char_number = char_number
        self.char_color = char_color
        self.char_type = char_type
        self.frame_delay = frame_delay
        self.bg_color = bg_color
        self.gradient = gradient
        self.start_text = start_text
        self.end_text = end_text

        if self.bg_color.lower() == 'random':
            self.bg_color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        if self.gradient.lower() == 'random':
            self.gradient = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

        self.frames = []
        self.answer = ''

    def generate_gradient(
        self, colour1: str, colour2: str, width: int, height: int) -> Image:
        """Generate a vertical gradient."""
        base = Image.new('RGB', (width, height), colour1)
        top = Image.new('RGB', (width, height), colour2)
        mask = Image.new('L', (width, height))
        mask_data = []
        for y in range(height):
            mask_data.extend([int(255 * (y / height))] * width)
        mask.putdata(mask_data)
        base.paste(top, (0, 0), mask)
        return base


    def calculate_position(self, fontsize, text = None):
        if len(text) > 1:
            x = 60
            y = int(self.width * 0.3)


            return x, y

        offset_x = int(self.width * 0.1)
        offset_y = int(self.height * 0.1)


        x = random.randint(0, self.width-offset_x-fontsize)
        y = random.randint(0, self.height-fontsize)


        return x, y


    def create_frame(self, text) -> None:
        if self.gradient:
            image = GifCaptcha.generate_gradient(
                self, self.gradient, self.bg_color, self.width, self.height)
        else:
            image = Image.new('RGB', (self.width, self.height), self.bg_color)

        draw = ImageDraw.Draw(image)

        fontsize = random.randint(int(self.height * 0.2), int(self.height * 0.4))
        x, y = GifCaptcha.calculate_position(self, fontsize, text)

        if self.char_color.lower() == 'random':
                #generate random hex color
                color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        else:
            color = self.char_color

        font = ImageFont.truetype('arial', fontsize)


        draw.text((x, y), text, color, font)

        self.frames.append(image)


    def Generate(self):

        if self.char_type == 1:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        elif self.char_type == 2:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXY'
        elif self.char_type == 3:
            chars = 'abcdefghijklmnopqrstuvwxyz'
        elif self.char_type == 4:
            chars = '0123456789'

        self.create_frame(self.start_text)

        for _ in range(self.char_number):
            text = random.choice(chars)
            self.create_frame(text)

            self.answer += text

        self.create_frame(self.end_text)



        #return gif using bytes.io and answer
        output = io.BytesIO()
        self.frames[0].save(output, format='GIF', append_images=self.frames[1:], save_all=True, duration=self.frame_delay, loop=0)
        output.seek(0)

        return FinishedCaptcha(output, self.answer)





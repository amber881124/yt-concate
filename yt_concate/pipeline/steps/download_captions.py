from pytube import YouTube

from .step import Step
from .step import StepException

import time

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            if utils.caption_file_exist(url):
                print('found existing caption file')
                continue
            try:
                # debug用的print
                print('downloading caption for', url)
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                # 沒拿到該影片的字幕'NoneType'
                print('AttributeError when downloading caption for', url)
                continue
            except KeyError:
                print('KeyError when downloading caption for', url)
                continue

            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        end = time.time()
        print(f'took {end - start} seconeds.')


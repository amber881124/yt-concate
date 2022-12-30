from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


# 檢查執行這個檔案時是不是程式的進入點
if __name__ == '__main__':
    main()

import os
import time
videosPath = '/Users/burak/Screenshots/videos'
imagesPath = '/Users/burak/Screenshots/images'
screenshotsPath = '/Users/burak/Screenshots'

def getScreenshots():
    return os.listdir(screenshotsPath)

def createMissingDirs():
    if not os.path.exists(videosPath):
        os.makedirs(videosPath)

    if not os.path.exists(imagesPath):
        os.makedirs(imagesPath)


def main():
    createMissingDirs()

    while True:
        screenshots = getScreenshots()

        if (len(screenshots) == 0):
            time.sleep(1)
            continue

        for screenshot in screenshots:
            if screenshot.endswith('.png'):
                os.rename(f'{screenshotsPath}/{screenshot}', f'{imagesPath}/{screenshot}')
            if screenshot.endswith('.mov'):
                os.replace(f'{screenshotsPath}/{screenshot}', f'{videosPath}/{screenshot}')
        
        time.sleep(1)

if __name__ == "__main__":
    main()


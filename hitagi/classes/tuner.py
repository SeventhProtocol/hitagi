import requests, subprocess, time

class Tuner:
    config = {}
    catalog = []
    tune_locks = {}

    default_ffmpeg_command = ["ffmpeg", "-threads", "4", "-f", "mpegts", "-analyzeduration", "2000000", "-i", "http://192.168.1.235:5004/auto/v502","-ac","2","-acodec","aac","-b:v","3000k","-bufsize","6000k","-minrate","2400k","-maxrate","3000k","-vcodec","libx264","-s","1280x720","-preset","superfast","-r","29.97","-async","1","-tune","zerolatency","-flags","-global_header","-fflags","+genpts","-map","0:0","-map","0:1","-strict","-2","/home/david/tmp/502.m3u8"

    def __init__(self, given_config):
        self.config = given_config

    def get_config(self):
        print(self.config)

    def fetch_catalog(self):
        catalog_url = self.config["tuner_url"] + "/lineup.json?show=subscribed"
        try:
            catalog_info = requests.get(catalog_url)
            for channel in catalog_info.json():
                if "DRM" in channel:
                    print("Channel '%s' has DRM, skipping." % channel["GuideName"])
                    continue
                self.catalog.append(channel)
            print("Successfully loaded catalog. There are %d channels available" % len(self.catalog))
        except:
            raise

    def tune_channel(self, channel):
        if channel in tune_locks:
            return "not yet implemented"
        
        tune_locks[channel] = {}
        tune_locks[channel]["time_started"] = int(time.time())
        ffmpeg_process = subprocess.Popen([], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        tune_locks[channel]["subprocess"] = ffmpeg_process
#      

import json
import os.path
from datetime import datetime
from glob import glob

class MetadataConverter():

    def __init__(self, animation_url_mime_type):
        self.animation_url_mime_type = animation_url_mime_type

    def convert(self, source_folder, destination_folder):
        os.makedirs(destination_folder, exist_ok=True)

        for src_file in glob(os.path.join(source_folder, "*.json")):
            dst_file = os.path.join(destination_folder, os.path.basename(src_file))
            self.convert_file(src_file, dst_file)

    def convert_file(self, src_file, dst_file):
        with open(src_file, "r", encoding="utf-8") as f:
            eth_metadata = json.load(f)

        imx_metadata = {
            k: v for k, v in {
                "name": eth_metadata.get("name"),
                "description": eth_metadata.get("description"),
                "image_url": eth_metadata.get("image"),
                "youtube_url": eth_metadata.get("youtube_url"),
            }.items() if v is not None
        }

        imx_metadata.update(self.convert_animation(eth_metadata.get("animation_url")))

        imx_metadata.update(self.convert_attributes(eth_metadata.get("attributes")))

        with open(dst_file, "w", encoding="utf-8") as f:
            json.dump(imx_metadata, f)

    def convert_animation(self, animation_url):
        if not animation_url:
            return {}

        if self.animation_url_mime_type:
            mime_type = self.animation_url_mime_type
        else:
            _base, extension = os.path.splitext(animation_url)
            extensions_mapping = {
                "m3u8": "application/vnd.apple.mpegurl",
                "m3u": "application/vnd.apple.mpegurl",
                "mp4": "video/mp4",
                "m4p": "video/mp4",
                "m4v": "video/mp4",
                "webm": "video/webm",
            }
            if extension in extensions_mapping:
                mime_type = extensions_mapping[extension]
            else:
                raise ValueError(
                    "Cannot determine animation mime type from extension, please specify --animation-url-mime-type"
                )

        return {
            "animation_url": animation_url,
            "animation_url_mime_type": mime_type,
        }

    def convert_attributes(self, attributes):
        if not attributes:
            return {}

        out = {}

        for attribute in attributes:
            key = attribute["trait_type"]
            value = attribute["value"]
            dtype = attribute.get("display_type", "text")

            if dtype == "date":
                value = datetime.fromtimestamp(value).isoformat()

            out[key] = value

        return out
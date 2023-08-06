import click

from metadata_converter import MetadataConverter

@click.command()
@click.argument('source-folder', default='source', required=True)
@click.argument('destination-folder', default='imx', required=False)
@click.option('--animation-url-mime-type', type=click.Choice(
    ['application/vnd.apple.mpegurl', 'video/mp4', 'video/webm']
), required=False)
def main(source_folder, destination_folder, animation_url_mime_type):
    """Tool for converting ERC-721 metadata format into Immutable X compatible format"""
    metadata_converter = MetadataConverter(animation_url_mime_type)
    metadata_converter.convert(source_folder, destination_folder)
    click.echo('Metadata converted')


if __name__ == "__main__":
    main()
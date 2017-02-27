"""Clip array using vector data."""
import numpy as np
import numpy.ma as ma
from shapely.geometry import shape, Polygon, MultiPolygon, GeometryCollection
from rasterio.features import geometry_mask


def clip_array_with_vector(
    array, array_affine, geometries, inverted=False, clip_buffer=0
):
    """
    Clip input array with a vector list.

    Parameters
    ----------
    array : array
        input raster data
    array_affine : Affine
        Affine object describing the raster's geolocation
    geometries : iterable
        iterable of dictionaries, where every entry has a 'geometry' and
        'properties' key.
    inverted : bool
        invert clip (default: False)
    clip_buffer : integer
        buffer (in pixels) geometries before clipping

    Returns
    -------
    clipped array : array
    """
    buffered_geometries = []
    # buffer input geometries and clean up
    for feature in geometries:
        geom = shape(feature['geometry']).buffer(clip_buffer)
        if not isinstance(geom, (Polygon, MultiPolygon, GeometryCollection)):
            break
        if geom.is_empty:
            break
        if isinstance(geom, GeometryCollection):
            polygons = [
                subgeom
                for subgeom in geom
                if isinstance(subgeom, (Polygon, MultiPolygon))
            ]
            if not polygons:
                break
            geom = MultiPolygon(polygons)
        buffered_geometries.append(geom)
    # mask raster by buffered geometries
    if buffered_geometries:
        if array.ndim == 2:
            return ma.masked_array(
                array, geometry_mask(
                    buffered_geometries, array.shape, array_affine,
                    invert=inverted))
        elif array.ndim == 3:
            mask = geometry_mask(
                buffered_geometries, (array.shape[1], array.shape[2]),
                array_affine, invert=inverted)
            return ma.masked_array(
                array, np.stack((mask for band in array))
            )
    # if no geometries, return unmasked array
    else:
        if inverted:
            fill = False
        else:
            fill = True
        return ma.masked_array(
            array, mask=np.full(array.shape, fill, dtype=bool))

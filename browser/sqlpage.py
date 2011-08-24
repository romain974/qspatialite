html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head>

	
		<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
		<title>SpatiaLite SQL functions reference list</title>
		<style type="text/css">
			h2 {color:navy; text-align:center;} 
			h3 {color:blue;} 
			i {color:navy;}
		</style>
	</head><body bgcolor="#fffff0">
		<h2>SpatiaLite 2.4.0-RC4: SQL functions reference list<span style="text-decoration: underline;"></span></h2>
<div style="text-align: center;"><span style="font-style: italic;">You'll find original page on the </span><a style="font-style: italic;" href="http://www.gaia-gis.it/spatialite/">SpatiaLite website</a><br>
</div>
<br>
<span style="font-weight: bold;">Important Note: In order to get a 
function in SQLeditor, double click on its name (it should be 
highlighted), and then simply drag and drop with mouse.</span><br>
<br>

		
		<ul>
			<li><a href="#version">SQL Version Info functions</a></li>
			<li><a href="#math">SQL math functions</a></li>
			<li><a href="#length_cvt">SQL length/distance unit-conversion functions</a></li>
			<li><a href="#blob">SQL utility functions for BLOB objects</a></li>
			<li><a href="#p0">SQL utility functions [non-standard] for geometric objects</a></li>
			<li><a href="#p1">SQL functions for constructing a geometric object given its Well-known Text Representation</a></li>
			<li><a href="#p2">SQL functions for constructing a geometric object given its Well-known Binary Representation</a></li>
			<li><a href="#p3">SQL functions for obtaining the Well-known Text / Well-known Binary Representation of a geometric object</a></li>
			<li><a href="#p3misc">SQL functions supporting exotic geometric formats</a></li>
			<li><a href="#p4">SQL functions on type Geometry</a></li>
			<li><a href="#repair">SQL functions attempting to repair malformed Geometries</a></li>
			<li><a href="#compress">SQL Geometry-compression functions</a></li>
			<li><a href="#cast">SQL Geometry-type casting functions</a></li>
			<li><a href="#dims-cast">SQL Space-dimensions casting functions</a></li>
			<li><a href="#p5">SQL functions on type Point</a></li>
			<li><a href="#p6">SQL functions on type Curve [Linestring or Ring]</a></li>
			<li><a href="#p7">SQL functions on type LineString</a></li>
			<li><a href="#p8">SQL functions on type Surface [Polygon or Ring]</a></li>
			<li><a href="#p9">SQL functions on type Polygon</a></li>
			<li><a href="#p10">SQL functions on type GeomCollection</a></li>
			<li><a href="#p11">SQL functions that test approximative spatial relationships via MBRs</a></li>
			<li><a href="#p12">SQL functions that test spatial relationships</a></li>
			<li><a href="#p13">SQL functions for distance relationships</a></li>
			<li><a href="#p14">SQL functions that implement spatial operators</a></li>
			<li><a href="#p15">SQL functions for coordinate transformations</a></li>
			<li><a href="#p16">SQL functions for Spatial-MetaData and Spatial-Index handling</a></li>
			<li><a href="#p16fdo">SQL functions implementing FDO/OGR compatibily</a></li>
			<li><a href="#p17">SQL functions for MbrCache-based queries</a></li>
			<li><a href="#p18">SQL functions for R*Tree-based queries (Geometry Callbacks)</a></li>
		</ul>
		<table bgcolor="#e2eae2" border="1" cellpadding="2" cellspacing="2" width="100%">
			<tbody><tr><td colspan="7" align="center" bgcolor="#f0e0c0">
				<h3><a name="version">SQL Version Info functions</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th colspan="5" bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>spatialite_version</td>
				<td>spatialite_version( void ) : <i>String</i></td>
				<td colspan="5">returns the current SpatiaLite version as a text string</td></tr>
			<tr><td>proj4_version</td>
				<td>proj4_version( void ) : <i>String</i></td>
				<td colspan="5">returns the current PROJ.4 version as a text string<br>
					or NULL if PROJ.4 is currently unsupported</td></tr>
			<tr><td>geos_version</td>
				<td>geos_version( void ) : <i>String</i></td>
				<td colspan="5">returns the current GEOS version as a text string<br>
					or NULL if GEOS is currently unsupported</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0e0c0">
				<h3><a name="math">SQL math functions</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th colspan="5" bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>Abs</td>
				<td>Abs( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the absolute value of x</td></tr>
			<tr><td>Acos</td>
				<td>Acos( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the arc cosine of x, that is, the value whose cosine is x<br>
				returns NULL if x is not in the range -1 to 1</td></tr>
			<tr><td>Asin</td>
				<td>Asin( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the arc sine of x, that is, the value whose sine is x<br>
				returns NULL if x is not in the range -1 to 1</td></tr>
			<tr><td>Atan</td>
				<td>Atan( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the arc tangent of x, that is, the value whose tangent is x</td></tr>
			<tr><td>Ceil<br>Ceiling</td>
				<td>Ceil( x <i>Double precision</i> ) : <i>Double precision</i><hr>
				Ceiling( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the smallest integer value not less than x</td></tr>
			<tr><td>Cos</td>
				<td>Cos( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the cosine of x, where x is given in <u>radians</u></td></tr>
			<tr><td>Cot</td>
				<td>Cot( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the cotangent of x, where x is given in <u>radians</u></td></tr>
			<tr><td>Degrees</td>
				<td>Degrees( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the argument x, converted from radians to degrees</td></tr>
			<tr><td>Exp</td>
				<td>Exp( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the value of <i>e</i> (the base of natural logarithms) raised to the power of x<hr>
				the inverse of this function is Log() (using a single argument only) or Ln()</td></tr>
			<tr><td>Floor</td>
				<td>Floor( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the largest integer value not greater than x</td></tr>
			<tr><td>Ln<br>Log</td>
				<td>Ln( x <i>Double precision</i> ) : <i>Double precision</i><hr>
				Log( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the natural logarithm of x; that is, the base-<i>e</i> logarithm of x<br>
				If x is less than or equal to 0, then NULL is returned</td></tr>
			<tr><td>Log</td>
				<td>Log( b <i>Double precision</i> , x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the logarithm of x to the base b<br>
				If x is less than or equal to 0, or if b is less than or equal to 1, then NULL is returned<hr>
				Log(b, x)  is equivalent to Log(x) / Log(b)</td></tr>
			<tr><td>Log2</td>
				<td>Log2( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the base-2 logarithm of x<hr>
				Log2(x)  is equivalent to Log(x) / Log(2)</td></tr>
			<tr><td>Log10</td>
				<td>Log10( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the base-10 logarithm of x<hr>
				Log10(x)  is equivalent to Log(x) / Log(10)</td></tr>
			<tr><td>PI</td>
				<td>PI( void ) : <i>Double precision</i></td>
				<td colspan="5">returns the value of PI</td></tr>
			<tr><td>Pow<br>Power</td>
				<td>Pow( x <i>Double precision</i> , y <i>Double precision</i> ) : <i>Double precision</i><hr>
				Power( x <i>Double precision</i> , y <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the value of x raised to the power of y</td></tr>
			<tr><td>Radians</td>
				<td>Radians( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the argument x, converted from degrees to radians</td></tr>
			<tr><td>Round</td>
				<td>Round( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the integer value nearest to x</td></tr>
			<tr><td>Sign</td>
				<td>Sign( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the sign of the argument as -1, 0, or 1, 
				depending on whether x is negative, zero, or positive. </td></tr>
			<tr><td>Sin</td>
				<td>Sin( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the sine of x, where x is given in <u>radians</u></td></tr>
			<tr><td>Sqrt</td>
				<td>Sqrt( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the square root of a non-negative number x</td></tr>
			<tr><td>Stddev_pop</td>
				<td>Stddev_pop( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the population standard deviation of the input values<br><u>aggregate function</u></td></tr>
			<tr><td>Stddev_samp</td>
				<td>Stddev_samp( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the sample standard deviation of the input values<br><u>aggregate function</u></td></tr>
			<tr><td>Tan</td>
				<td>Tan( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the tangent of x, where x is given in <u>radians</u></td></tr>
			<tr><td>Var_pop</td>
				<td>Var_pop( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the population variance of the input values (<i>square of the population standard deviation</i>)<br>
				<u>aggregate function</u></td></tr>
			<tr><td>Var_samp</td>
				<td>Var_samp( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">returns the sample variance of the input values (<i>square of the sample standard deviation</i>)<br>
				<u>aggregate function</u></td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0e0c0">
				<h3><a name="length_cvt">SQL length/distance unit-conversion functions</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th colspan="5" bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>Kilometer</td>
				<td>CvtToKm( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromKm( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / kilometers</td></tr>
			<tr><td>Decimeter</td>
				<td>CvtToDm( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromDm( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / decimeters</td></tr>
			<tr><td>Centimeter</td>
				<td>CvtToCm( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromCm( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / centimeters</td></tr>
			<tr><td>Millimeter</td>
				<td>CvtToMm( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromMm( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / millimeters</td></tr>
			<tr><td>International Nautical Mile</td>
				<td>CvtToKmi( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromKmi( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / international nautical miles</td></tr>
			<tr><td>International Inch</td>
				<td>CvtToIn( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromIn( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / international inches</td></tr>
			<tr><td>International Foot</td>
				<td>CvtToFt( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromFt( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / international feet</td></tr>
			<tr><td>International Yard</td>
				<td>CvtToYd( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromYd( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / international yards</td></tr>
			<tr><td>International Statute Mile</td>
				<td>CvtToMi( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromMi( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / international statute miles</td></tr>
			<tr><td>International Fathom</td>
				<td>CvtToFath( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromFath( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / international fathoms</td></tr>
			<tr><td>International Chain</td>
				<td>CvtToCh( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromCh( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / international chains</td></tr>
			<tr><td>International Link</td>
				<td>CvtToLink( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromLink( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / international links</td></tr>
			<tr><td>U.S. Inch</td>
				<td>CvtToUsIn( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromUsIn( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / U.S. inches</td></tr>
			<tr><td>U.S. Foot</td>
				<td>CvtToUsFt( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromUsFt( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / U.S. feet</td></tr>
			<tr><td>U.S. Yard</td>
				<td>CvtToUsYd( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromUsYd( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / U.S. yards</td></tr>
			<tr><td>U.S. Statute Mile</td>
				<td>CvtToUsMi( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromUsMi( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / U.S. statute miles</td></tr>
			<tr><td>U.S. Chain</td>
				<td>CvtToUsCh( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromUsCh( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / U.S. chains</td></tr>
			<tr><td>Indian Foot</td>
				<td>CvtToIndFt( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromIndFt( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / indian feet</td></tr>
			<tr><td>Indian Yard</td>
				<td>CvtToIndYd( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromIndYd( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / indian yards</td></tr>
			<tr><td>Indian Chain</td>
				<td>CvtToIndCh( x <i>Double precision</i> ) : <i>Double precision</i><hr>
					CvtFromIndCh( x <i>Double precision</i> ) : <i>Double precision</i></td>
				<td colspan="5">meters / indian chains</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0e0c0">
				<h3><a name="blob">SQL utility functions for BLOB objects</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th colspan="5" bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>IsZipBlob</td>
				<td>IsZipBlob( content <i>BLOB</i> ) : <i>Integer</i></td>
				<td colspan="5">The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL or not-BLOB argument.<hr>
					TRUE if this BLOB object corresponds to a valid ZIP-compressed file</td></tr>
			<tr><td>IsPdfBlob</td>
				<td>IsPdfBlob( content <i>BLOB</i> ) : <i>Integer</i></td>
				<td colspan="5">The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL or not-BLOB argument.<hr>
					TRUE if this BLOB object corresponds to a valid PDF document</td></tr>
			<tr><td>IsGifBlob</td>
				<td>IsGifBlob( image <i>BLOB</i> ) : <i>Integer</i></td>
				<td colspan="5">The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL or not-BLOB argument.<hr>
					TRUE if this BLOB object corresponds to a valid GIF image</td></tr>
			<tr><td>IsPngBlob</td>
				<td>IsPngBlob( image <i>BLOB</i> ) : <i>Integer</i></td>
				<td colspan="5">The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL or not-BLOB argument.<hr>
					TRUE if this BLOB object corresponds to a valid PNG image</td></tr>
			<tr><td>IsTiffBlob</td>
				<td>IsTiffBlob( image <i>BLOB</i> ) : <i>Integer</i></td>
				<td colspan="5">The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL or not-BLOB argument.<hr>
					TRUE if this BLOB object corresponds to a valid TIFF image</td></tr>
			<tr><td>IsJpegBlob</td>
				<td>IsJpegBlob( image <i>BLOB</i> ) : <i>Integer</i></td>
				<td colspan="5">The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL or not-BLOB argument.<hr>
					TRUE if this BLOB object corresponds to a valid JPEG image</td></tr>
			<tr><td>IsExifBlob</td>
				<td>IsExifBlob( image <i>BLOB</i> ) : <i>Integer</i></td>
				<td colspan="5">The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL or not-BLOB argument.<hr>
					TRUE if this BLOB object corresponds to a valid EXIF image<br>
					<u>Please note:</u> any valid EXIF image is a valid JPEG as well</td></tr>
			<tr><td>IsExifGpsBlob</td>
				<td>IsExifGpsBlob( image <i>BLOB</i> ) : <i>Integer</i></td>
				<td colspan="5">The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL or not-BLOB argument.<hr>
					TRUE if this BLOB object corresponds to a valid EXIF-GPS image<br>
					<u>Please note:</u> any valid EXIF-GPS image is a valid EXIF and JPEG as well</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p0">SQL utility functions [<i>non-standard</i>] for geometric objects</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>GeomFromExifGpsBlob</td>
				<td>GeomFromExifGpsBlob( image <i>BLOB</i> ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>a POINT Geometry will be returned representing the GPS long/lat contained within EXIF-GPS <i>metadata</i>
				for the BLOB image<hr>
				NULL will be returned if for any reason it's not possible to build such a POINT</td></tr>
			<tr><td>MakePoint</td>
				<td>MakePoint( x <i>Double precision</i> , y <i>Double precision</i> ,
				[ , SRID <i>Integer</i>] ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>a Geometry will be returned representing the POINT defined by [x y] coordinates</td></tr>
			<tr><td>BuildArea</td>
				<td>BuildArea( geom <i>Geometry</i>) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>a Geometry (actually corresponding to a <i>POLYGON</i> or <i>MULTIPOLYGON</i>) will be returned.<br>
				The input Geometry is expected to represent a <i>LINESTRING</i> or a <i>MULTILINESTRING</i>: 
				each linestring has to be closed [i.e. it must represent a <i>RING</i>].<hr>
				NULL will be returned if any error is encountered</td></tr>
			<tr><td>Polygonize</td>
				<td>Polygonize( geom <i>Geometry</i>) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>a Geometry (actually corresponding to a <i>POLYGON</i> or <i>MULTIPOLYGON</i>) will be returned.<br>
				The input Geometry is expected to represent a <i>LINESTRING</i> or a <i>MULTILINESTRING</i>.<br> 
				The input Geometry can be an arbitrary collection of sparse Linestrings: this
				function will then try to (possibly) reassemble them into one (or more) polygon(s).<hr>
				NULL will be returned if any error is encountered</td></tr>
			<tr><td>BuildMbr</td>
				<td>BuildMbr( x1 <i>Double precision</i> , y1 <i>Double precision</i> ,
				x2 <i>Double precision</i> , y2 <i>Double precision</i> [ , SRID <i>Integer</i>] ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>[x1 y1] and [x2 y2] are assumed to be Points identifying a line segment;
then a Geometry will be returned representing the MBR for this line segment</td></tr>
			<tr><td>BuildCircleMbr</td>
				<td>BuildCircleMbr( x <i>Double precision</i> , y <i>Double precision</i> ,
				radius <i>Double precision</i> [ , SRID <i>Integer</i>] ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>[x y] is assumed to be the center of a circle of given radius;
then a Geometry will be returned representing the MBR for this circle</td></tr>
			<tr><td>MbrMinX</td>
				<td>MbrMinX( geom <i>Geometry</i>) : <i>Double precision</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the x-coordinate for <i>geom</i> MBR's <u>leftmost side</u> as a double precision number</td></tr>
			<tr><td>MbrMinY</td>
				<td>MbrMinY( geom <i>Geometry</i>) : <i>Double precision</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the y-coordinate for <i>geom</i> MBR's <u>lowermost side</u> as a double precision number</td></tr>
			<tr><td>MbrMaxX</td>
				<td>MbrMaxX( geom <i>Geometry</i>) : <i>Double precision</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the x-coordinate for <i>geom</i> MBR's <u>rightmost side</u> as a double precision number</td></tr>
			<tr><td>MbrMaxY</td>
				<td>MbrMaxY( geom <i>Geometry</i>) : <i>Double precision</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the y-coordinate for <i>geom</i> MBR's <u>uppermost side</u> as a double precision number</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p1">SQL functions for constructing a geometric object given its Well-known Text Representation</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>GeomFromText</td>
				<td>GeomFromText( wkt <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Geometry</i><hr>
					ST_GeomFromText( wkt <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a geometric object given its Well-known text Representation</td></tr>
			<tr><td>PointFromText</td>
				<td>PointFromText( wktPoint <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Point</i><hr>
					ST_PointFromText( wktPoint <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Point</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a Point</td></tr>
			<tr><td>LineFromText<br>LineStringFromText</td>
				<td>LineFromText( wktLineString <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Linestring</i><hr>
					ST_LineFromText( wktLineString <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Linestring</i><hr>
					LineStringFromText( wktLineString <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Linestring</i><hr>
					ST_LineStringFromText( wktLineString <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Linestring</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a Linestring</td></tr>
			<tr><td>PolyFromText<br>PolygonFromText</td>
				<td>PolyFromText( wktPolygon <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i><hr>
					ST_PolyFromText( wktPolygon <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i><hr>
					PolygonFromText( wktPolygon <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i><hr>
					ST_PolygonFromText( wktPolygon <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a Polygon</td></tr>
			<tr><td>MPointFromText<br>MultiPointFromText</td>
				<td>MPointFromText( wktMultiPoint <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPoint</i><hr>
					ST_MPointFromText( wktMultiPoint <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPoint</i><hr>
					MultiPointFromText( wktMultiPoint <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPoint</i><hr>
					ST_MultiPointFromText( wktMultiPoint <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPoint</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a MultiPoint</td></tr>
			<tr><td>MLineFromText<br>MultiLineStringFromText</td>
				<td>MLineFromText( wktMultiLineString <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiLinestring</i><hr>
					ST_MLineFromText( wktMultiLineString <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiLinestring</i><hr>
					MultiLineStringFromText( wktMultiLineString <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiLinestring</i><hr>
					ST_MultiLineStringFromText( wktMultiLineString <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiLinestring</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a MultiLinestring</td></tr>
			<tr><td>MPolyFromText<br>MultiPolygonFromText</td>
				<td>MPolyFromText( wktMultiPolygon <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i><hr>
					ST_MPolyFromText( wktMultiPolygon <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i><hr>
					MultiPolygonFromText( wktMultiPolygon <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i><hr>
					ST_MultiPolygonFromText( wktMultiPolygon <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a MultiPolygon</td></tr>
			<tr><td>GeomCollFromText<br>GeometryCollectionFromText</td>
				<td>GeomCollFromText( wktGeometryCollection <i>String</i> [ , SRID <i>Integer</i>] ) : <i>GeometryCollection</i><hr>
					ST_GeomCollFromText( wktGeometryCollection <i>String</i> [ , SRID <i>Integer</i>] ) : <i>GeometryCollection</i><hr>
					GeometryCollectionFromText( wktGeometryCollection <i>String</i> [ , SRID <i>Integer</i>] ) : <i>GeometryCollection</i><hr>
					ST_GeometryCollectionFromText( wktGeometryCollection <i>String</i> [ , SRID <i>Integer</i>] ) : <i>GeometryCollection</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a GeometryCollection</td></tr>
			<tr><td>BdPolyFromText</td>
				<td>BdPolyFromText( wktMultilinestring <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i><hr>
					ST_BdPolyFromText( wktMultilinestring <i>String</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Construct a Polygon given an arbitrary collection of closed linestrings as a MultiLineString text representation.
				<hr><i>see also</i>: BuildArea(), Polygonize()</td></tr>
			<tr><td>BdMPolyFromText</td>
				<td>BdMPolyFromText( wktMultilinestring <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i><hr>
					ST_BdMPolyFromText( wktMultilinestring <i>String</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Construct a MultiPolygon given an arbitrary collection of closed linestrings as a MultiLineString text representation.
				<hr><i>see also</i>: BuildArea(), Polygonize()</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p2">SQL functions for constructing a geometric object given its Well-known Binary Representation</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>GeomFromWKB</td>
				<td>GeomFromWKB( wkbGeometry <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Geometry</i><hr>
					ST_GeomFromWKB( wkbGeometry <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a geometric object given its Well-known binary Representation</td></tr>
			<tr><td>PointFromWKB</td>
				<td>PointFromWKB( wkbPoint <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Point</i><hr>
					ST_PointFromWKB( wkbPoint <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Point</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a Point</td></tr>
			<tr><td>LineFromWKB<br>LineStringFromWKB</td>
				<td>LineFromWKB( wkbLineString <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Linestring</i><hr>
					ST_LineFromWKB( wkbLineString <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Linestring</i><hr>
					LineStringFromText( wkbLineString <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Linestring</i><hr>
					ST_LineStringFromText( wkbLineString <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Linestring</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a Linestring</td></tr>
			<tr><td>PolyFromWKB<br>PolygonFromWKB</td>
				<td>PolyFromWKB( wkbPolygon <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i><hr>
					ST_PolyFromWKB( wkbPolygon <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i><hr>
					PolygonFromWKB( wkbPolygon <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i><hr>
					ST_PolygonFromWKB( wkbPolygon <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a Polygon</td></tr>
			<tr><td>MPointFromWKB<br>MultiPointFromWKB</td>
				<td>MPointFromWKB( wkbMultiPoint <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPoint</i><hr>
					ST_MPointFromWKB( wkbMultiPoint <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPoint</i><hr>
					MultiPointFromWKB( wkbMultiPoint <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPoint</i>
					ST_MultiPointFromWKB( wkbMultiPoint <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPoint</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a MultiPoint</td></tr>
			<tr><td>MLineFromWKB<br>MultiLineStringFromWKB</td>
				<td>MLineFromWKB( wkbMultiLineString <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiLinestring</i><hr>
					ST_MLineFromWKB( wkbMultiLineString <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiLinestring</i><hr>
					MultiLineStringFromWKB( wkbMultiLineString <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiLinestring</i><hr>
					ST_MultiLineStringFromWKB( wkbMultiLineString <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiLinestring</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a MultiLinestring</td></tr>
			<tr><td>MPolyFromWKB<br>MultiPolygonFromWKB</td>
				<td>MPolyFromWKB( wkbMultiPolygon <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i><hr>
					ST_MPolyFromWKB( wkbMultiPolygon <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i><hr>
					MultiPolygonFromWKB( wkbMultiPolygon <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i><hr>
					ST_MultiPolygonFromWKB( wkbMultiPolygon <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a MultiPolygon</td></tr>
			<tr><td>GeomCollFromWKB<br>GeometryCollectionFromWKB</td>
				<td>GeomCollFromWKB( wkbGeometryCollection <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>GeometryCollection</i><hr>
					ST_GeomCollFromWKB( wkbGeometryCollection <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>GeometryCollection</i><hr>
					GeometryCollectionFromWKB( wkbGeometryCollection <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>GeometryCollection</i><hr>
					ST_GeometryCollectionFromWKB( wkbGeometryCollection <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>GeometryCollection</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a GeometryCollection</td></tr>
			<tr><td>BdPolyFromWKB</td>
				<td>BdPolyFromWKB( wkbMultilinestring <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i><hr>
					ST_BdPolyFromWKB( wkbMultilinestring <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Polygon</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Construct a Polygon given an arbitrary collection of closed linestrings as a MultiLineString binary representation.
				<hr><i>see also</i>: BuildArea(), Polygonize()</td></tr>
			<tr><td>BdMPolyFromWKB</td>
				<td>BdMPolyFromWKB( wkbMultilinestring <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i><hr>
					ST_BdMPolyFromWKB( wkbMultilinestring <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>MultiPolygon</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Construct a MultiPolygon given an arbitrary collection of closed linestrings as a MultiLineString binary representation.
				<hr><i>see also</i>: BuildArea(), Polygonize()</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p3">SQL functions for obtaining the Well-known Text / Well-known Binary Representation of a geometric object</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>AsText</td>
				<td>AsText( geom <i>Geometry</i> ) : <i>String</i><hr>
					ST_AsText( geom <i>Geometry</i> ) : <i>String</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the Well-known Text representation</td></tr>
			<tr><td>AsBinary</td>
				<td>AsBinary( geom <i>Geometry</i> ) : <i>Binary</i><hr>
					ST_AsBinary( geom <i>Geometry</i> ) : <i>Binary</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the Well-known Binary representation</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p3misc">SQL functions supporting exotic geometric formats</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>AsSVG</td>
				<td>AsSVG( geom <i>Geometry</i> [ , relative <i>Integer</i> [ , precision <i>Integer</i> ] ] ) : <i>String</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the SVG [<i>Scalable Vector Graphics</i>] representation</td></tr>
			<tr><td>AsKml</td>
				<td>AsKml( geom <i>Geometry</i> [ , precision <i>Integer</i> ] ) : <i>String</i><br>
				AsKml( name <i>String</i>, desc <i>String</i>, geom <i>Geometry</i> [ , precision <i>Integer</i> ] ) : <i>String</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the KML [<i>Keyhole Markup Language</i>] representation<br>
				The first form will simply generate the geometry element: the second form will generate a complete KML entity</td></tr>
			<tr><td>AsGml</td>
				<td>AsGml( geom <i>Geometry</i> [ , precision <i>Integer</i> ] ) : <i>String</i><br>
				AsGml( version <i>Integer</i>, geom <i>Geometry</i> [ , precision <i>Integer</i> ] ) : <i>String</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the GML [<i>Geography Markup Language</i>] representation<br>
				If <i>version = 3</i> than GML 3.x is generated, otherwise the output format will be GML 2.x</td></tr>
			<tr><td>AsFGF</td>
				<td>AsFGF( geom <i>Geometry</i> ) : <i>Binary</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the FGF [<i>FDO Geometry Binary Format</i>] representation</td></tr>
			<tr><td>GeomFromFGF</td>
				<td>GeomFromFGF( fgfGeometry <i>Binary</i> [ , SRID <i>Integer</i>] ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>construct a geometric object given its FGF binary Representation</td></tr>	
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p4">SQL functions on type Geometry</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>Dimension</td>
				<td>Dimension( geom <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Dimension( geom <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the dimension of the geometric object, which is less than or equal to the dimension 
					of the coordinate space</td></tr>
			<tr><td>CoordDimension</td>
				<td>CoordDimension( geom <i>Geometry</i> ) : <i>String</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the dimension model used by the geometric object as:<br>
					'XY', 'XYZ', 'XYM' or 'XYZM'</td></tr>
			<tr><td>GeometryType</td>
				<td>GeometryType( geom <i>Geometry</i> ) : <i>String</i><hr>
					ST_GeometryType( geom <i>Geometry</i> ) : <i>String</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the name of the instantiable subtype of Geometry of which this geometric object is a member, as a string</td></tr>
			<tr><td>SRID</td>
				<td>SRID( geom <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_SRID( geom <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the Spatial Reference System ID for this geometric object</td></tr>
			<tr><td>SetSRID</td>
				<td>SetSRID( geom <i>Geometry</i> , SRID <i>Integer</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>directly sets the Spatial Reference System ID for this geometric object [no reprojection is applied]<hr>
					The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL arguments.</td></tr>
			<tr><td>IsEmpty</td>
				<td>IsEmpty( geom <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_IsEmpty( geom <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL arguments.<hr>
					TRUE if this geometric object corresponds to the empty set</td></tr>
			<tr><td>IsSimple</td>
				<td>IsSimple( geom <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_IsSimple( geom <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL arguments.<hr>
					TRUE if this geometric object is simple, as defined in the Geometry Model</td></tr>
			<tr><td>IsValid</td>
				<td>IsValid( geom <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_IsValid( geom <i>Geometry</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL arguments.<hr>
					TRUE if this geometric object does  not contains any topological error</td></tr>
			<tr><td>Boundary</td>
				<td>Boundary( geom <i>Geometry</i> ) : <i>Geometry</i><hr>
					ST_Boundary( geom <i>Geometry</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns a geometric object that is the combinatorial boundary of g as defined in the Geometry Model</td></tr>
			<tr><td>Envelope</td>
				<td>Envelope( geom <i>Geometry</i> ) : <i>Geometry</i><hr>
					ST_Envelope( geom <i>Geometry</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>returns the rectangle bounding g as a Polygon. The Polygon is defined by the corner points of the bounding
					box [(MINX, MINY),(MAXX, MINY), (MAXX, MAXY), (MINX, MAXY), (MINX, MINY)].</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="repair">SQL functions attempting to repair malformed Geometries</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>SanitizeGeometry</td>
				<td>SanitizeGeometry( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a (possibly) sanitized Geometry [<i>if a valid Geometry was supplied</i>], or NULL in any other case<hr>
					<u>Please note</u>: current implementations only affects:<ul>
						<li>repeated vertices suppression</li>
						<li>Ring's closure enforcement</li>
					</ul></td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="compress">SQL Geometry-compression functions</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>CompressGeometry</td>
				<td>CompressGeometry( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a compressed Geometry [<i>if a valid Geometry was supplied</i>], or NULL in any other case<hr>
					<u>Please note</u>: geometry compression only affects LINESTRINGs and POLYGONs, not POINTs</td></tr>
			<tr><td>UncompressGeometry</td>
				<td>UncompressGeometry( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns an uncompressed Geometry [<i>if a valid Geometry was supplied</i>], or NULL in any other case</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="cast">SQL Geometry-type casting functions</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>CastToPoint</td>
				<td>CastToPoint( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a POINT-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					can be applied to any Geometry containing only a single POINT and no other elementary sub-geometry</td></tr>
			<tr><td>CastToLinestring</td>
				<td>CastToLinestring( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a LINESTRING-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					can be applied to any Geometry containing only a single LINESTRING and no other elementary sub-geometry</td></tr>
			<tr><td>CastToPolygon</td>
				<td>CastToPolygon( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a POLYGON-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					can be applied to any Geometry containing only a single POLYGON and no other elementary sub-geometry</td></tr>
			<tr><td>CastToMultiPoint</td>
				<td>CastToMultiPoint( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a MULTIPOINT-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					can be applied to any Geometry containing one or more POINT(s) and no other elementary sub-geometry</td></tr>
			<tr><td>CastToMultiLinestring</td>
				<td>CastToMultiLinestring( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a MULTILINESTRING-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					can be applied to any Geometry containing one or more LINESTRING(s) and no other elementary sub-geometry</td></tr>
			<tr><td>CastToMultiPolygon</td>
				<td>CastToMultiPolygon( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a MULTIPOLYGON-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					can be applied to any Geometry containing one or more POLYGON(s) and no other elementary sub-geometry</td></tr>
			<tr><td>CastToGeometyCollection</td>
				<td>CastToGeometryCollection( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a GEOMETRYCOLLECTION-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					can be applied to any valid Geometry</td></tr>
			<tr><td>CastToMulti</td>
				<td>CastToMulti( geom <i>Geometry</i> ) : geom <i>Geometry</i><hr>
					ST_Multi( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a MULTIPOINT-, MULTILINESTRING- or MULTIPOLYGON-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					<ul>
					<li>a MULTIPOINT will be returned for a Geometry containing one or more POINT(s) and no other elementary sub-geometry</li>
					<li>a MULTILINESTRING will be returned for a Geometry containing one or more LINESTRING(s) and no other elementary sub-geometry</li>
					<li>a MULTIPOLYGON will be returned for a Geometry containing one or more POLYGON(s) and no other elementary sub-geometry</li>
					<li>a GEOMETRYCOLLECTION will be returned for any other valid Geometry</li>
					</ul></td></tr>
			<tr><td>CastToSingle</td>
				<td>CastToSingle( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a POINT-, LINESTRING- or POLYGON-type Geometry [<i>if type-conversione is possible</i>], or NULL in any other case<hr>
					<ul>
					<li>a POINT will be returned for a Geometry containing only a single POINT and no other elementary sub-geometry</li>
					<li>a LINESTRING will be returned for a Geometry containing only a single LINESTRING and no other elementary sub-geometry</li>
					<li>a POLYGON will be returned for a Geometry containing only a single POLYGON and no other elementary sub-geometry</li>
					</ul></td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="dims-cast">SQL Space-dimensions casting functions</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>CastToXY</td>
				<td>CastToXY( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a Geometry using the [XY] space dimension</td></tr>
			<tr><td>CastToXYZ</td>
				<td>CastToXYZ( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a Geometry using the [XYZ] space dimension</td></tr>
			<tr><td>CastToXYM</td>
				<td>CastToXYM( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a Geometry using the [XYZM] space dimension</td></tr>
			<tr><td>CastToXYZM</td>
				<td>CastToXYZM( geom <i>Geometry</i> ) : geom <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>returns a Geometry using the [XYZM] space dimension</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p5">SQL functions on type Point</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>X</td>
				<td>X( pt <i>Point</i> ) : <i>Double precision</i><hr>
					ST_X( pt <i>Point</i> ) : <i>Double precision</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the x-coordinate of Point p as a double precision number</td></tr>
			<tr><td>Y</td>
				<td>Y( pt <i>Point</i> ) : <i>Double precision</i><hr>
					ST_Y( pt <i>Point</i> ) : <i>Double precision</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the y-coordinate of Point p as a double precision number</td></tr>
			<tr><td>Z</td>
				<td>Z( pt <i>Point</i> ) : <i>Double precision</i><hr>
					ST_Z( pt <i>Point</i> ) : <i>Double precision</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the z-coordinate of Point p as a double precision number<br>
					or NULL is no z-coordinate is available</td></tr>
			<tr><td>M</td>
				<td>M( pt <i>Point</i> ) : <i>Double precision</i><hr>
					ST_M( pt <i>Point</i> ) : <i>Double precision</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the m-coordinate of Point p as a double precision number<br>
					or NULL is no m-coordinate is available</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p6">SQL functions on type Curve [Linestring or Ring]</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>StartPoint</td>
				<td>StartPoint( c <i>Curve</i> ) : <i>Point</i><hr>
					ST_StartPoint( c <i>Curve</i> ) : <i>Point</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a Point containing the first Point of c</td></tr>
			<tr><td>EndPoint</td>
				<td>EndPoint( c <i>Curve</i> ) : <i>Point</i><hr>
					ST_EndPoint( c <i>Curve</i> ) : <i>Point</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a Point containing the last Point of c</td></tr>
			<tr><td>Length</td>
				<td>GLength( c <i>Curve</i> ) : <i>Double precision</i>
					<table><tbody><tr><td bgcolor="#d080ff">
						OpenGis name for this function is Length(), but it conflicts with an SQLite reserved keyword
					</td></tr></tbody></table><hr>
					ST_Length( c <i>Curve</i> ) : <i>Double precision</i>
				</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the length of c</td></tr>
			<tr><td>Geodesic Length</td>
				<td>GeodesicLength( c <i>Curve</i> ) : <i>Double precision</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>If [<i>and only if</i>] the SRID associated with <i>c</i> is a geographic one [<i>i.e. one using longitude and latitude angles</i>],
				then returns the length of <i>c</i> measured on the Ellipsoid [<i>such length is always expressed in meters</i>]<br>
				Otherwise NULL will be returned<hr>
				<u>Please note:</u> measuring lengths on the Ellipsoid requires complex geodesic calculations, and thus is an
				intrinsecally <u>slow and time consuming</u> task</td></tr>
			<tr><td>Great Circle Length</td>
				<td>GreatCircleLength( c <i>Curve</i> ) : <i>Double precision</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td>If [<i>and only if</i>] the SRID associated with <i>c</i> is a geographic one [<i>i.e. one using longitude and latitude angles</i>],
				then returns the length of <i>c</i> measured on the Great Circle [<i>such length is always expressed in meters</i>]<br>
				Otherwise NULL will be returned<hr>
				<u>Please note:</u>
lengths measured on the Great Circle are less precise then lengths
measured on the Ellipsoid using complex geodesic calculations; but they
are by far quickest to compute</td></tr>
			<tr><td>IsClosed</td>
				<td>IsClosed( c <i>Curve</i> ) : <i>Integer</i><hr>
					ST_IsClosed( c <i>Curve</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL arguments;<hr>
					return TRUE if c is closed, i.e., if StartPoint(c) = EndPoint(c)</td></tr>
			<tr><td>IsRing</td>
				<td>IsRing( c <i>Curve</i> ) : <i>Integer</i><hr>
					ST_IsRing( c <i>Curve</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, and &#8211;1 for UNKNOWN
					corresponding to a function invocation on NULL arguments.<hr>
					return TRUE if c is a ring, i.e., if c is closed and simple. A simple Curve does not pass through 
					the same Point more than once.</td></tr>
			<tr><td>Simplify</td>
				<td>Simplify( c <i>Curve</i> , tolerance <i>Double precision</i> ) : <i>Curve</i><hr>
				ST_Generalize( c <i>Curve</i> , tolerance <i>Double precision</i> ) : <i>Curve</i></td>
				<td><br>
</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object representing a simplified version of <i>c</i> applying the Douglas-Peukert 
algorithm with given <i>tolerance</i></td></tr>
			<tr><td>SimplifyPreserveTopology</td>
				<td>SimplifyPreserveTopology( c <i>Curve</i> , tolerance <i>Double precision</i> ) : <i>Curve</i></td>
				<td><br>
</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object representing a simplified version of <i>c</i> applying the Douglas-Peukert 
algorithm with given <i>tolerance</i> and respecting topology</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p7">SQL functions on type LineString</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>NumPoints</td>
				<td>NumPoints( line <i>LineString</i> ) : <i>Integer</i><hr>
					ST_NumPoints( line <i>LineString</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the number of Points in the LineString</td></tr>
			<tr><td>PointN</td>
				<td>PointN( line <i>LineString</i> , n <i>Integer</i> ) : <i>Point</i><hr>
					ST_PointN( line <i>LineString</i> , n <i>Integer</i> ) : <i>Point</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a Point containing Point n of line</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p8">SQL functions on type Surface [Polygon or Ring]</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>Centroid</td>
				<td>Centroid( s <i>Surface</i> ) : <i>Point</i><hr>
					ST_Centroid( s <i>Surface</i> ) : <i>Point</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the centroid of s, which may lie outside s</td></tr>
			<tr><td>PointOnSurface</td>
				<td>PointOnSurface( s <i>Surface</i> ) : <i>Point</i><hr>
					ST_PointOnSurface( s <i>Surface</i> ) : <i>Point</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a Point guaranteed to lie on the Surface</td></tr>
			<tr><td>Area</td>
				<td>Area( s <i>Surface</i> ) : <i>Double precision</i><hr>
					ST_Area( s <i>Surface</i> ) : <i>Double precision</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the area of s</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p9">SQL functions on type Polygon</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>ExteriorRing</td>
				<td>ExteriorRing( polyg <i>Polygon</i> ) : <i>LineString</i><hr>
					ST_ExteriorRing( polyg <i>Polygon</i> ) : <i>LineString</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the exteriorRing of p</td></tr>
			<tr><td>NumInteriorRing<br>NumInteriorRings</td>
				<td>NumInteriorRing( polyg <i>Polygon</i> ) : <i>Integer</i><hr>
					NumInteriorRings( polyg <i>Polygon</i> ) : <i>Integer</i><hr>
					ST_NumInteriorRing( polyg <i>Polygon</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the number of interiorRings</td></tr>
			<tr><td>InteriorRingN</td>
				<td>InteriorRingN( polyg <i>Polygon</i> , n <i>Integer</i> ) : <i>LineString</i><hr>
					ST_InteriorRingN( polyg <i>Polygon</i> , n <i>Integer</i> ) : <i>LineString</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the nth interiorRing. The order of Rings is not geometrically significant.</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p10">SQL functions on type GeomCollection</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>NumGeometries</td>
				<td>NumGeometries( geom <i>GeomCollection</i> ) : <i>Integer</i><hr>
					ST_NumGeometries( geom <i>GeomCollection</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the number of interiorRings</td></tr>
			<tr><td>GeometryN</td>
				<td>GeometryN( geom <i>GeomCollection</i> , n <i>Integer</i> ) : <i>Geometry</i><hr>
					ST_GeometryN( geom <i>GeomCollection</i> , n <i>Integer</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the nth geometric object in the collection.
					The order of the elements in the collection is not geometrically significant.</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p11">SQL functions that test approximative spatial relationships via MBRs</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>MbrEqual</td>
				<td>MbrEqual( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if g1 and g2 have equal MBRs</td></tr>
			<tr><td>MbrDisjoint</td>
				<td>MbrDisjoint( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if the intersection of g1 and g2 MBRs is the empty set</td></tr>
			<tr><td>MbrTouches</td>
				<td>MbrTouches( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if the only Points in common between g1 and g2 MBRs lie in the union of the boundaries of g1 and g2</td></tr>
			<tr><td>MbrWithin</td>
				<td>MbrWithin( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if g1 MBR is completely contained in g2 MBR</td></tr>
			<tr><td>MbrOverlaps</td>
				<td>MbrOverlaps( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if the intersection of g1 and g2 MBRs results in a value of the same
					dimension as g1 and g2 that is different from both g1 and g2</td></tr>
			<tr><td>MbrIntersects</td>
				<td>MbrIntersects( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments;<br>
					convenience predicate: TRUE if the intersection of g1 and g2 MBRs is not empty</td></tr>
			<tr><td>MbrContains</td>
				<td>MbrContains( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments;<hr>
					convenience predicate: TRUE if g2 MBR is completely contained in g1 MBR</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p12">SQL functions that test spatial relationships</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>Equals</td>
				<td>Equals( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Equals( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if g1 and g2 are equal</td></tr>
			<tr><td>Disjoint</td>
				<td>Disjoint( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Disjoint( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if the intersection of g1 and g2 is the empty set</td></tr>
			<tr><td>Touches</td>
				<td>Touches( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Touches( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if the only Points in common between g1 and g2 lie in the union of the boundaries of g1 and g2</td></tr>
			<tr><td>Within</td>
				<td>Within( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Within( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if g1 is completely contained in g2</td></tr>
			<tr><td>Overlaps</td>
				<td>Overlaps( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Overlaps( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if the intersection of g1 and g2 results in a value of the same
					dimension as g1 and g2 that is different from both g1 and g2</td></tr>
			<tr><td>Crosses</td>
				<td>Crosses( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Crosses( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments.<hr>
					TRUE if the intersection of g1 and g2 results in a value whose dimension is less 
					than the maximum dimension of g1 and g2 and the intersection value includes Points 
					interior to both g1 and g2, and the intersection value is not equal to either g1 or g2</td></tr>
			<tr><td>Intersects</td>
				<td>Intersects( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Intersects( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments;<br>
					convenience predicate: TRUE if the intersection of g1 and g2 is not empty</td></tr>
			<tr><td>Contains</td>
				<td>Contains( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i><hr>
					ST_Contains( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments;<hr>
					convenience predicate: TRUE if g2 is completely contained in g1</td></tr>
			<tr><td>Relate</td>
				<td>Relate( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> , patternMatrix <i>String</i> ) : <i>Integer</i><hr>
					ST_Relate( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> , patternMatrix <i>String</i> ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>The return type is Integer, with a return value of 1 for TRUE, 0 for FALSE, 
					and &#8211;1 for UNKNOWN corresponding to a function invocation on NULL arguments;<hr>
					returns TRUE if the spatial relationship specified by the patternMatrix holds</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p13">SQL functions for distance relationships</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>Distance</td>
				<td>Distance( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Double precision</i><hr>
					ST_Distance( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Double precision</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return the distance between geom1 and geom2</td></tr>
			<tr><td>PtDistWithin</td>
				<td>PtDistWithin( geom1 <i>Geometry</i> , geom2 <i>Geometry</i>, range <i>Double precision</i> [, use_spheroid <i>Integer</i> ] ) 
					: <i>Integer</i></td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td>return TRUE (1) if the distance between <i>geom1</i> and <i>geom2</i> is within the given range.<br>
				Usually distances are expressed in the length unit correspondind to the geoms own SRID:
				but if both geoms are simple POINTs and their SRID is 4326 (i.e. WGS84), then distances are
				expressed in meters.<br>
				In this later case the optional arg <i>use_spheroid</i> can be used to select the distance
				algorithm to be used: is <i>use_spheroid = 1</i> the slowest but most accurate geodesic distance
				will be evaluated: in any other case the simplest great circle distance will be used instead</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p14">SQL functions that implement spatial operators</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>Intersection</td>
				<td>Intersection( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Geometry</i><hr>
					ST_Intersection( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object that is the intersection of geometric objects geom1 and geom2</td></tr>
			<tr><td>Difference</td>
				<td>Difference( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Geometry</i><hr>
					ST_Difference( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object that is the closure of the set difference of geom1 and geom2</td></tr>
			<tr><td>GUnion</td>
				<td>GUnion( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Geometry</i>
					<table><tbody><tr><td bgcolor="#d080ff">
						OpenGis name for this function is Union(), but it conflicts with an SQLite reserved keyword
					</td></tr></tbody></table><hr>
					ST_Union( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Geometry</i>
				</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object that is the set union of geom1 and geom2</td></tr>
			<tr><td>GUnion</td>
				<td>GUnion( geom <i>Geometry</i> ) : <i>Geometry</i><hr>
					ST_Union( geom <i>Geometry</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object that is the set union of input values
				<u>aggregate function</u></td></tr>
			<tr><td>SymDifference</td>
				<td>SymDifference( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Geometry</i><hr>
					ST_SymDifference( geom1 <i>Geometry</i> , geom2 <i>Geometry</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object that is the closure of the set symmetric difference of geom1 and geom2 
					(logical XOR of space)</td></tr>
			<tr><td>Buffer</td>
				<td>Buffer( geom <i>Geometry</i> , dist <i>Double precision</i> ) : <i>Geometry</i><hr>
					ST_Buffer( geom <i>Geometry</i> , dist <i>Double precision</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object defined by buffering a distance d around geom, 
					where dist is in the distance units for the Spatial Reference of geom</td></tr>
			<tr><td>ConvexHull</td>
				<td>ConvexHull( geom <i>Geometry</i> ) : <i>Geometry</i><hr>
					ST_ConvexHull( geom <i>Geometry</i> ) : <i>Geometry</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object that is the convex hull of geom</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p15">SQL functions for coordinate transformations</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>Transform</td>
				<td>Transform( geom <i>Geometry</i> , newSRID <i>Integer</i> ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td><br>
</td>
				<td>return a geometric object obtained by reprojecting coordinates into the Reference System identified by newSRID</td></tr>
			<tr><td>ShiftCoords<br>ShiftCoordinates</td>
				<td>ShiftCoords( geom <i>Geometry</i> , shiftX <i>Double precision</i> , shiftY <i>Double precision</i> ) : <i>Geometry</i><hr>
					ShiftCoordinates( geom <i>Geometry</i> , shiftX <i>Double precision</i> , shiftY <i>Double precision</i> ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object obtained by translating coordinates according to shiftX and shiftY values</td></tr>
			<tr><td>ScaleCoords<br>ScaleCoordinates</td>
				<td>ScaleCoords( geom <i>Geometry</i> , scaleX <i>Double precision</i> [ , scaleY <i>Double precision</i> ] ) : <i>Geometry</i><hr>
					ScaleCoordinates( geom <i>Geometry</i> , scaleX <i>Double precision</i> [ , scaleY <i>Double precision</i> ] ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object obtained by scaling coordinates according to scaleX and scaleY values<hr>
					if only one scale factor is specified, then an <i>isotropic</i> scaling occurs 
					[i.e. the same scale factor is applied to both axis]<br>
					otherwise an <i>anisotropic</i> scaling occurs [i.e. each axis is scaled according to its own scale factor]</td></tr>
			<tr><td>RotateCoords<br>RotateCoordinates</td>
				<td>RotateCoords( geom <i>Geometry</i> , angleInDegrees <i>Double precision</i> ) : <i>Geometry</i><hr>
					RotateCoordinates( geom <i>Geometry</i> , angleInDegrees <i>Double precision</i> ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object obtained by rotating coordinates according to angleInDegrees value</td></tr>
			<tr><td>ReflectCoords<br>ReflectCoordinates</td>
				<td>ReflectCoords( geom <i>Geometry</i> , xAxis <i>Integer</i> , yAxis <i>Integer</i> ) : <i>Geometry</i><hr>
					ReflectCoordinates( geom <i>Geometry</i> , xAxis <i>Integer</i> , yAxis <i>Integer</i> ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object obtained by reflecting coordinates according to xAxis and yAxis switches<hr>
					i.e. if xAxis is 0 (FALSE), then x-coordinates remains untouched; otherwise x-coordinates will be reflected</td></tr>
			<tr><td>SwapCoords<br>SwapCoordinates</td>
				<td>SwapCoords( geom <i>Geometry</i> ) : <i>Geometry</i><hr>
					SwapCoordinates( geom <i>Geometry</i> ) : <i>Geometry</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>return a geometric object obtained by swapping x- and y-coordinates</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p16">SQL functions for Spatial-MetaData and Spatial-Index handling</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>InitSpatialMetaData</td>
				<td>InitSpatialMetaData( void ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Creates the geometry_columns and spatial_ref_sys metadata tables<br>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE<hr>
direct invocation of these function is <u>discouraged</u>; you have to run the init_spatialite.sql
script in order to fully initialize the Spatial MetaData tables</td></tr>
			<tr><td>AddGeometryColumn</td>
				<td>AddGeometryColumn( table <i>String</i> , column <i>String</i> , srid <i>Integer</i> ,
geom_type <i>String</i> , dimension <i>String</i> [ , not_null <i>Integer</i> ] ) : <i>Integer</i></td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Creates a new <u>geometry column</u> updating the Spatial Metadata tables and creating any
required <u>trigger</u> in order to enforce constraints<hr>
				geom_type has to be one of the followings:<ul>
				<li>'POINT'</li>
				<li>'LINESTRING'</li>
				<li>'POLYGON'</li>
				<li>'MULTIPOINT'</li>
				<li>'MULTILINESTRING'</li>
				<li>'MULTIPOLYGON'</li>
				<li>'GEOMETRYCOLLECTION'</li>
				</ul>dimension has to be one of the followings:
				<ul>
				<li>'XY' or 2: 2D points, identified by X and Y coordinates</li>
				<li>'XYM': 2D points, identified by X and Y coordinates. 
				Each point stores an M-value (<i>measure</i>) as well</li>
				<li>'XYZ' or 3: 3D points, identified by X, Y and Z coordinates</li>
				<li>'XYZM': 3D points, identified by X, Y and Z coordinates. 
				Each point stores an M-value (<i>measure</i>) as well</li>
				</ul><hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE<hr>
the optional 6th arg [not_null] is a non-standard extension required by the peculiar SQLite arch:<ul>
				<li>if set to 0 [<i>false</i>], then the Geometry column will accept NULL values as well.
					This is the <u>default</u> behaviour</li>
				<li>if set to any &lt;&gt; 0 value [<i>true</i>], then the Geometry will be defined using a NOT NULL clause</li>
				</ul></td></tr>
			<tr><td>RecoverGeometryColumn</td>
				<td>RecoverGeometryColumn( table <i>String</i> , column <i>String</i> , srid <i>Integer</i> ,
geom_type <i>String</i> , dimension <i>Integer</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Validates an existing ordinary column in order to possibly transform it in a real <u>geometry column</u>,
thus updating the Spatial Metadata tables and creating any required <u>trigger</u> in order to enforce constraints<hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE</td></tr>
			<tr><td>DiscardGeometryColumn</td>
				<td>DiscardGeometryColumn( table <i>String</i> , column <i>String</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Removes a <u>geometry column</u> from Spatial MetaData tables and drops any related <u>trigger</u><br>
the column itself still continues to exist untouched as an ordinary, unconstrained column<hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE</td></tr>
			<tr><td>CreateSpatialIndex</td>
				<td>CreateSpatialIndex( table <i>String</i> , column <i>String</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Builds an RTree Spatial Index on a <u>geometry column</u>, creating any required <u>trigger</u>
required in order to enforce full data coherency between the main table and Spatial Index<hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE</td></tr>
			<tr><td>CreateMbrCache</td>
				<td>CreateMbrCache( table <i>String</i> , column <i>String</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Builds an MbrCache on a <u>geometry column</u>, creating any required <u>trigger</u>
required in order to enforce full data coherency between the main table and the MbrCache<hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE</td></tr>
			<tr><td>DisableSpatialIndex</td>
				<td>DisableSpatialIndex( table <i>String</i> , column <i>String</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Disables an RTree Spatial Index or MbrCache, removing any related <u>trigger</u><hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p16fdo">SQL functions implementing FDO/OGR compatibily</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>CheckSpatialMetaData</td>
				<td>CheckSpatialMetaData( void ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Checks the Spatial Metadata type, then returning:<ul>
				<li>0 - if geometry_columns and spatial_ref_sys tables does not exists</li>
				<li>1 - if both tables exist, and their layout is the one used by SpatiaLite</li>
				<li>2 - if both tables exist, and their layout is the one used by FDO/OGR</li>
				</ul></td></tr>
			<tr><td>AutoFDOStart</td>
				<td>AutoFDOStart( void ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>This function will inspect the Spatial Metadata, then automatically creating/refreshing a VirtualFDO
				wrapper for each FDO/OGR geometry table<hr>
the return type is Integer [how many VirtualFDO tables have been created]</td></tr>
			<tr><td>AutoFDOStop</td>
				<td>AutoFDOStop( void ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>This function will inspect the Spatial Metadata, then automatically destroying any VirtualFDO
				wrapper found<hr>
the return type is Integer [how many VirtualFDO tables have been destroyed]</td></tr>
			<tr><td>InitFDOSpatialMetaData</td>
				<td>InitFDOSpatialMetaData( void ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Creates the geometry_columns and spatial_ref_sys metadata tables<br>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE<hr>
<u>Please note:</u> Spatial Metadata created using this function will have the FDO/OGR layout, and not the SpatiaLite's own</td></tr>
			<tr><td>AddFDOGeometryColumn</td>
				<td>AddFDOGeometryColumn( table <i>String</i> , column <i>String</i> , srid <i>Integer</i> ,
geom_type <i>Integer</i> , dimension <i>Integer</i>, geometry_format <i>String</i> ) : <i>Integer</i> </td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Creates a new <u>geometry column</u> updating the FDO/OGR Spatial Metadata tables<hr>
				geom_type has to be one of the followings:<ul>
				<li>1 <i>POINT</i></li>
				<li>2 <i>LINESTRING</i></li>
				<li>3 <i>POLYGON</i></li>
				<li>4 <i>MULTIPOINT</i></li>
				<li>5 <i>MULTILINESTRING</i></li>
				<li>6 <i>MULTIPOLYGON</i></li>
				<li>7 <i>GEOMETRYCOLLECTION</i></li>
				</ul>dimension may be 2, 3 or 4, accordingly to OGR/FDO specs<br>
				geometry_format has to be one of the followings:<ul>
				<li>'WBT'</li>
				<li>'WKT'</li>
				<li>'FGF'</li>
				</ul><hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE</td></tr>
			<tr><td>RecoverFDOGeometryColumn</td>
				<td>RecoverFDOGeometryColumn( table <i>String</i> , column <i>String</i> , srid <i>Integer</i> ,
geom_type <i>String</i> , dimension <i>Integer</i>, geometry_format <i>String</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Validates an existing ordinary column in order to possibly transform it in a real <u>geometry column</u>,
thus updating the FDO/OGR Spatial Metadata tables<hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE</td></tr>
			<tr><td>DiscardFDOGeometryColumn</td>
				<td>DiscardFDOGeometryColumn( table <i>String</i> , column <i>String</i> ) : <i>Integer</i></td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Removes a <u>geometry column</u> from FDO/OGR Spatial MetaData tables<br>
the column itself still continues to exist untouched as an ordinary column<hr>
the return type is Integer, with a return value of 1 for TRUE or 0 for FALSE</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p17">SQL functions for MbrCache-based queries</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>FilterMbrWithin</td>
				<td>FilterMbrWithin(  x1 <i>Double precision</i> , y1 <i>Double precision</i> ,
				x2 <i>Double precision</i> , y2 <i>Double precision</i> )</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Retrieves from an MbrCache any entity whose MBR falls <u><i>within</i></u>
				the rectangle identified by extreme points x1 y1 and x2 y2</td></tr>
			<tr><td>FilterMbrContains</td>
				<td>FilterMbrContains(  x1 <i>Double precision</i> , y1 <i>Double precision</i> ,
				x2 <i>Double precision</i> , y2 <i>Double precision</i> )</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Retrieves from an MbrCache any entity whose MBR <u><i>contains</i></u>
				the rectangle identified by extreme points x1 y1 and x2 y2</td></tr>
			<tr><td>FilterMbrIntersects</td>
				<td>FilterMbrIntersects(  x1 <i>Double precision</i> , y1 <i>Double precision</i> ,
				x2 <i>Double precision</i> , y2 <i>Double precision</i> )</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Retrieves from an MbrCache any entity whose MBR <u><i>intersects</i></u>
				the rectangle identified by extreme points x1 y1 and x2 y2</td></tr>
			<tr><td>BuildMbrFilter</td>
				<td>BuildMbrFilter(  x1 <i>Double precision</i> , y1 <i>Double precision</i> ,
				x2 <i>Double precision</i> , y2 <i>Double precision</i> )</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Creates an MBR identified by extreme points x1 y1 and x2 y2<hr>
				This fuction is used internally by <u><i>triggers</i></u> related to MbrCache management,
				and is not intended for any other usage</td></tr>
			<tr><td colspan="7" align="center" bgcolor="#f0f0c0">
				<h3><a name="p18">SQL functions for R*Tree-based queries (Geometry Callbacks)</a></h3></td></tr>
			<tr><th bgcolor="#d0d0d0">Function</th>
				<th bgcolor="#d0d0d0">Syntax</th>
				<th bgcolor="#d0d0d0">OpenGis<br>defined</th>
				<th bgcolor="#d0d0d0">SpatiaLite<br>base</th>
				<th bgcolor="#d0d0d0">PROJ<br>included</th>
				<th bgcolor="#d0d0d0">GEOS<br>included</th>
				<th bgcolor="#d0d0d0">Summary</th></tr>
			<tr><td>RTreeIntersects</td>
				<td>RTreeIntersects(  x1 <i>Double precision</i> , y1 <i>Double precision</i> ,
				x2 <i>Double precision</i> , y2 <i>Double precision</i> )</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Retrieves from an R*Tree Spatial Index any entity whose MBR <u><i>intersect</i></u>
				the rectangle identified by extreme points x1 y1 and x2 y2</td></tr>
			<tr><td>RTreeWithin</td>
				<td>RTreeWithin(  x1 <i>Double precision</i> , y1 <i>Double precision</i> ,
				x2 <i>Double precision</i> , y2 <i>Double precision</i> )</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Retrieves from an R*Tree Spatial Index any entity whose MBR falls <u><i>within</i></u>
				the rectangle identified by extreme points x1 y1 and x2 y2</td></tr>
			<tr><td>RTreeContain</td>
				<td>RTreeContain(  x1 <i>Double precision</i> , y1 <i>Double precision</i> ,
				x2 <i>Double precision</i> , y2 <i>Double precision</i> )</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Retrieves from an R*Tree Spatial Index any entity whose MBR <u><i>contain</i></u>
				the rectangle identified by extreme points x1 y1 and x2 y2</td></tr>
			<tr><td>RTreeDistWithin</td>
				<td>RTreeDistWithin(  x <i>Double precision</i> , y <i>Double precision</i> ,
				radius <i>Double precision</i> )</td>
				<td><br>
</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td align="center" bgcolor="#d0f0d0">X</td>
				<td>Retrieves from an R*Tree Spatial Index any entity whose MBR <u><i>intersect</i></u>
				the square circumscribed on the given circle (x y center, radius)</td></tr>
		</tbody></table>
	</body></html>
"""

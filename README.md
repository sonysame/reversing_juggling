###reversing_juggling

XML: Extensible Markup Language

XSLT: Extensible Stylesheet Language Transformation

XSLT can transform the XML document!

We can infer the structure of the XML document with the analysis of the XSLT. The following is the inferred structure of the XML document.
```xml
<?xml version="1.0" encoding="UTF-8"?>
    <meal>
        <course>
            <plate>
                <paella>1</paella>
    			<Борщ>2</Борщ>
    			<宫保鸡丁>3</宫保鸡丁>
            </plate>
    		<plate>
    			<दाल>1</दाल>
    			<paella>4</paella>
    		</plate>
        </course>
        <state>
            <drinks>1</drinks>
            <drinks>2</drinks>
        </state>
	</meal>
```
Now, we have to figure out what is related to the flag. If the number of $chef-drinks is 0, we can get the flag.
```xml
<xsl:when test="count($c/दाल) = 1">
	<xsl:if test="count($chef-drinks) = 0">
		<xsl:copy-of select="document('/flag')" />
	</xsl:if>
```
$chef-drinks is initialized with the five random values, so the number of $chef-drinks is 5. 
```xml
<xsl:variable name="chef-drinks">
	<value>
	    <xsl:value-of select="round(math:random() * 4294967296)" />
	</value>
	<value>
	    <xsl:value-of select="round(math:random() * 4294967296)" />
	</value>
	<value>
	    <xsl:value-of select="round(math:random() * 4294967296)" />
	</value>
	<value>
	    <xsl:value-of select="round(math:random() * 4294967296)" />
	</value>
	<value>
	    <xsl:value-of select="round(math:random() * 4294967296)" />
	</value>
```
$chef-drinks only changes in the case of **count($c/Борщ) = 1**. When $chef-drinks[1] is equal to $drinks[1], the head of the $chef-drinks will be removed. Therefore, we have to know $chef-drinks[1] in order to remove the head of $chef-drinks. If we repeat 5 times, we could totally remove the $chef-drinks. 

```xml
<xsl:when test="count($c/Борщ) = 1">
    <xsl:variable name="arg0">
        <value>
            <xsl:value-of select="$drinks[1] + 0" />
        </value>
    </xsl:variable>
    <xsl:call-template name="consume-meal">
        <xsl:with-param name="chef-drinks" select="$chef-drinks[position() &gt; 1 or $chef-drinks[1] != $arg0]" />
```
Let's see how each important case works.

case | function
--------- | ---------
count($c/宫保鸡丁) = 1 |  print out $chef-drinks and $drinks
count($c/paella) = 1 | append certain data to $drinks
count($c/ラーメン) = 1 | append 1 to $drinks if $drinks[1] is greater than $chef-drinks[1]. If not, append 0.  Moreover, remove the head of $drinks.
count($c/Борщ) = 1 | remove the head of $chef-drinks if $drinks[1] is equal to $chef-drinks[1]. Moreover, remove the head of $drinks.
count($c/दाल) = 1 | get the flag if count($chef-drinks) = 0

We can control $drinks by using paella, and we can know the initialized value of $chef-drinks by using 宫保鸡丁. When I try to execute this program several times immediately, the values of $chef-drinks are constant. The $chef-drinks[1] will be the first part of the printed $chef-drinks. However, we do now know the length of each 5 values of thw $chef-drinks. By using ラーメン, we can check the length of the $chef-drinks[1]. Usually, the length does not exceed 10. So we will assume that first 10 digits of the printed $chef-drinks is the $chef-drinks[1] and we can check if it is true by using ラーメン. If the result is false, we will reduce the length of $chef-drinks[1]. Repeat this 5 times, we could get the total 5 values of the $chef-drinks and make $chef-drinks NULL by using Борщ 5 times. Finally we can get the flag!
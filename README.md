#reversing_juggling
\#xml \#xslt \#reversing 

###challenge.min.xslt
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:math="http://exslt.org/math" xmlns:exsl="http://exslt.org/common" exclude-result-prefixes="xsl math exsl">
    <xsl:template match="/meal">
        <all>
            <xsl:if test="count(//plate) &gt; 300">
                <xsl:message terminate="yes">You do not have enough money to buy that much food</xsl:message>
            </xsl:if>
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
            </xsl:variable>
            <xsl:call-template name="consume-meal">
                <xsl:with-param name="chef-drinks" select="exsl:node-set($chef-drinks)//value" />
                <xsl:with-param name="food-eaten" select="1" />
                <xsl:with-param name="course" select="course[position() = 1]/plate" />
                <xsl:with-param name="drinks" select="state/drinks" />
            </xsl:call-template>
        </all>
    </xsl:template>
    <xsl:template name="consume-meal">
        <xsl:param name="chef-drinks" />
        <xsl:param name="food-eaten" />
        <xsl:param name="course" />
        <xsl:param name="drinks" />
        <xsl:if test="$food-eaten &gt; 30000">
            <xsl:message terminate="yes">You ate too much and died</xsl:message>
        </xsl:if>
        <xsl:if test="count($drinks) &gt; 200">
            <xsl:message terminate="yes">You cannot drink that much</xsl:message>
        </xsl:if>
        <xsl:if test="count($course) &gt; 0">
            <xsl:variable name="c" select="$course[1]" />
            <xsl:variable name="r" select="$course[position()&gt;1]" />
            <xsl:choose>
                <xsl:when test="count($c/宫保鸡丁) = 1">
                    <xsl:message>
                        <chef-drinks>
                            <xsl:copy-of select="$chef-drinks" />
                        </chef-drinks>
                    </xsl:message>
                    <xsl:message>
                        <drinks>
                            <xsl:copy-of select="$drinks" />
                        </drinks>
                    </xsl:message>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="$drinks" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/paella) = 1">
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$c/paella + 0" />
                        </value>
                        <xsl:copy-of select="$drinks" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/불고기) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$drinks[$arg0 + 2] + 0" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 1]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/Борщ) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks[position() &gt; 1 or $chef-drinks[1] != $arg0]" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="$drinks[position() &gt; 1]" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/दाल) = 1">
                    <xsl:if test="count($chef-drinks) = 0">
                        <xsl:copy-of select="document('/flag')" />
                    </xsl:if>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="$drinks" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/ラーメン) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="chefvalue">
                        <value>
                            <xsl:value-of select="$chef-drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="1 * ($arg0 &gt; $chefvalue)" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 1]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/stroopwafels) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="1 * ($arg1 &gt; $arg0)" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/köttbullar) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <xsl:copy-of select="$drinks[($arg1+3) &gt; position() and position() &gt; 2]" />
                        <value>
                            <xsl:value-of select="$arg0" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt;= ($arg1 + 3)]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/γύρος) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="$drinks[position() &gt; 1 and position() != ($arg0 + 2)]" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/rösti) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$arg0 + $arg1" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/לאַטקעס) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$arg0 - $arg1" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/poutine) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$arg0 * $arg1" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/حُمُّص) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="floor($arg0 div $arg1)" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/æblegrød) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:choose>
                        <xsl:when test="$arg0 != 0">
                            <xsl:call-template name="consume-meal">
                                <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                                <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                                <xsl:with-param name="course" select="/meal/course[position() = ($arg1+1)]/plate" />
                                <xsl:with-param name="drinks" select="$drinks[position() &gt; 2]" />
                            </xsl:call-template>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:call-template name="consume-meal">
                                <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                                <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                                <xsl:with-param name="course" select="$r" />
                                <xsl:with-param name="drinks" select="$drinks[position() &gt; 2]" />
                            </xsl:call-template>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:when>
            </xsl:choose>
        </xsl:if>
    </xsl:template>
</xsl:stylesheet>
```

XML: Extensible Markup Language
XSLT: Extensible Stylesheet Language Transformation

XSLT can transform the XML document!

We can infer the structure of the XML document with the analysis of the XSLT. The following is the inferred structrue of the XML document.
```xml
<?xml version="1.0" encoding="UTF-8"?>
	<meal>
		<course>
			<plate>
				<paella>1</paella>
				<Борщ>2</Борщ>s
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
$chef-drinks is initialized with the five random values so the number of $chef-drinks if 5. 
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
$chef-drinks only changes in the case of **count($c/Борщ) = 1** when $chef-drinks[1] is equal to $drinks[1]. The head of the $chef-drinks will be removed. Therefore, we have to know $chef-drinks[1] to remove the head of $chef-drinks. If we repeat 5 times, we will totally remove the $chef-drinks. 

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
count($c/宫保鸡丁) = 1|  print out $chef-drinks and $drinks
count($c/paella) = 1 | append certain data to $drinks
count($c/ラーメン) = 1 | remove the head of $drinks and append 1 to $drinks if $drinks[1] is greater than $chef-drinks[1]. If not, append 0.  Moreover, remove the head of $drinks.
count($c/Борщ) = 1| remove the head of $chef-drinks if $drinks[1] is equal to $chef-drinks[1]. Moreover, remove the head of $drinks.
count($c/दाल) = 1 | get the flag if count($chef-drinks) = 0

We can control $drinks by using paella, and we can know the initialized value of $chef-drinks by using 宫保鸡丁. When I try to execute this program several times immediately, the values of $chef-drinks are constant.$chef-drinks[1] will be the first part of the printed  $chef-drinks. However, we do now know the length of each 5 values of $chef-drinks. By using ラーメン, we can check the length of $chef-drinks[1]. Usually, the length does not exceed 10. So we will assume that the first 10 digits of the printed $chef-drinks is  $chef-drinks[1] and check if it is true by using ラーメン. If the result is false, we will reduce the length of $chef-drinks[1]. Repeat this 5 times, we can get the total 5 parts of $chef-drinks and make $chef-drinks NULL by using Борщ, and finally get the flag!. 
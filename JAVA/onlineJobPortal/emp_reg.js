<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1" import = "java.sql.*"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3c.org/TR/1999/REC-html401-19991224/loose.dtd">
<HTML><HEAD><FONT SIZE="4"COLOR="blue" FACE="roman">Candidate Information Page : 
</FONT>

<TITLE>APPLICANT LOGIN PAGE</TITLE>
<META content="text/html; charset=windows-1252" http-equiv=Content-Type>
<META name=GENERATOR content="MSHTML 9.00.8080.16413"></HEAD>
<BODY BGCOLOR="#4EE2EC" >
<form NAME="CREATEACCTFORM" action="emp_reg.jsp"  METHOD="POST" >
<table width="780" border="0" align="center" cellpadding="0" cellspacing="0">
	

	

	<table width="100%" border="0" cellpadding="7" cellspacing="0" class="bg_white">

	  <tr>
		  <td colspan="2" align="right" valign="top" class="border_green_btm bg_grey" style="padding:0px 10px 0px 0px;"><span class="txt_orange">*</span> Required fields</td>

		</tr>
	  
<tr>
				<td width="400" align="right" bgcolor="#736AFF">Login Information</td>
				
			</tr>

			 

<tr>
				<td align="right" valign="top"><span class="txt_orange">*</span> Desired username:</td>
				<td valign="top"  ><input maxlength="255" size="30" name="username"   onFocus="hintEvent('UNAME');"  onblur="hintEvent('UNAME', 'HIDE');" type="text" value="">
					<div id="UNAME" style="width:250px; margin-left:205px; margin-top:-20px; _margin-left:20px; _margin-top:0px; position:absolute;"></div>

					<div id="ERR_UNAME" style="padding: 2px; width: 400px; display: none;" class="txt_red small_1"></div>
				</td>

			  </tr>
			  <tr>

				<td align="right" valign="top"><span class="txt_orange">*</span> Choose a password: </td>
				<td valign="top"  >
				<input maxlength="32" size="30"  name="passwd" type="password" value="">

				<div id="PASS" style="width:250px; margin-left:205px; margin-top:-20px; _margin-left:20px; _margin-top:0px; position:absolute;"></div>

				<div id="ERR_PASS" style="padding: 2px; width: 400px; display: none;" class="txt_red small_1"></div>
				</td>
			</tr>
			  <tr>
				<td align="right" valign="top"><span class="txt_orange">*</span> Re-enter password: </td>
				<td valign="top"  >

				<input name="passwd_temp"   size="30" maxlength="32" type="password"  value="">

				<div id="PASS_TEMP" style="width:250px; margin-left:205px; margin-top:-20px; _margin-left:20px; _margin-top:0px; position:absolute;"></div>
				<div id="ERR_PASS_TEMP" style="padding: 2px; width: 400px; display: none;" class="txt_red small_1"></div>
				</td>

			</tr>


			<tr>
				<td align="right" valign="top"><span class="txt_orange">* </span>
				Web address: </td>
				
				<td  >

				<table cellspacing="0" cellpadding="0" border="0" id="currentloc_border">
				<tr><td>
				<input type="text" name="web" value="">
				</table>

					 </td>

			</tr>
	<table width="350" border="0" cellpadding="0" cellspacing="0">


						<tr>
                <td valign="bottom" class="bg_grey" >&nbsp;</td>

                <td height="40" valign="bottom"  class="bg_grey"><span class="button"><span>
				<input type="submit" name="submit1"  value="Submit"></span></span>
				</td>

			 
</table>
<%

String s1=request.getParameter("username");
String s2=request.getParameter("passwd");
String s3=request.getParameter("web");
out.println(s1);
out.println(s2);
if(s1!=null && s2!=null && s3!=null )
{
try{
	out.println("success");
	Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
	Connection c=DriverManager.getConnection("jdbc:odbc:abc","root","root");
	Statement s =c.createStatement();
	String sql = "insert into employer values('"+s1+"','"+s2+"','"+s3+"')";
	s.execute(sql);
	
}catch(Exception e ){out.println(e);}
}
%>

</table>
</form>
<form method="post" action="done_emp.jsp">
<table cellspacing="0" cellpadding="0" border="0" id="currentloc_border">
				<tr><td>
				<BR>&nbsp<input type="submit" value="SUBMIT">
				</table>

</form>
</body>
</html>

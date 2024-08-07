<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="com.dp.crud.model.User" %>
<%@ page import="com.dp.crud.dao.UserDao" %>
<%
    int id = Integer.parseInt(request.getParameter("id"));
    UserDao userDao = new UserDao();
    User user = userDao.getUserById(id);
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Edit User</title>
</head>
<body>
    <h2>Edit User</h2>
    <form action="editUser" method="post">
        <input type="hidden" name="id" value="<%= user.getId() %>">
        Name: <input type="text" name="name" value="<%= user.getName() %>"><br>
        Email: <input type="text" name="email" value="<%= user.getEmail() %>"><br>
        <input type="submit" value="Update">
    </form>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.List" %>
<%@ page import="com.dp.crud.model.User" %>
<%@ page import="com.dp.crud.dao.UserDao" %>
<%
    UserDao userDao = new UserDao();
    List<User> users = userDao.getAllUsers();
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>List Users</title>
</head>
<body>
    <h2>List of Users</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Actions</th>
        </tr>
        <%
            for (User user : users) {
        %>
        <tr>
            <td><%= user.getId() %></td>
            <td><%= user.getName() %></td>
            <td><%= user.getEmail() %></td>
            <td>
                <a href="editUser?id=<%= user.getId() %>">Edit</a>
                <a href="deleteUser?id=<%= user.getId() %>">Delete</a>
            </td>
        </tr>
        <%
            }
        %>
    </table>
    <a href="add-user.jsp">Add New User</a>
</body>
</html>
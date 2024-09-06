import 'package:flutter/material.dart';
import 'package:application/screen/register.dart'; 

void main() => runApp(MaterialApp( 
      debugShowCheckedModeBanner: false, 
      initialRoute: '/', 
      routes: {'/': (context) => const Register()}, 
    )); 
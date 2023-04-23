<!DOCTYPE html>
<html>
  <head>
    <title>Password Generator</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
      }
      
      header {
        background-color: #24292E;
        color: #fff;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
      }
      
      header h1 {
        margin: 0;
        font-size: 3rem;
      }
      
      .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
      }
      
      h2 {
        font-size: 2rem;
        margin-top: 30px;
      }
      
      p {
        font-size: 1.2rem;
        line-height: 1.5;
      }
      
      pre {
        background-color: #f4f4f4;
        padding: 10px;
        overflow-x: auto;
      }
      
      code {
        background-color: #f4f4f4;
        padding: 2px 5px;
        border-radius: 5px;
      }
      
      .features {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
      }
      
      .feature {
        background-color: #f4f4f4;
        padding: 20px;
        margin: 10px;
        border-radius: 5px;
        width: 47%;
      }
      
      .feature h3 {
        font-size: 1.5rem;
        margin-top: 0;
      }
      
      .feature p {
        margin: 0;
        font-size: 1rem;
        line-height: 1.5;
      }
      
      .feature pre {
        margin-top: 10px;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Password Generator</h1>
    </header>
    <div class="container">
      <h2>Description</h2>
      <p>This is a simple password generator written in Python. The program generates a random password based on user input for length and password complexity. The password can include lowercase letters, uppercase letters, numbers, and special characters.</p>
      
      <h2>Usage</h2>
      <p>The program can be run from the command line. To run the program, enter the following command:</p>
      <pre><code>python password_generator.py</code></pre>
      
      <p>The program will then prompt you for the following input:</p>
      <ul>
        <li>Password length</li>
        <li>Include lowercase letters (Y/N)</li>
        <li>Include uppercase letters (Y/N)</li>
        <li>Include numbers (Y/N)</li>
        <li>Include special characters (Y/N)</li>
      </ul>
      
      <p>After entering the input, the program will generate a random password and display it on the screen.</p>
      
      <h2>Features</h2>
      <div class="features">
        <div class="feature">
          <h3>Customizable Password Length</h3>
          <p>The program allows you to specify the length of the password. You can generate passwords with a length of up to 128 characters.</p>
          <pre><code>python password_generator.py</code></pre>
        </div


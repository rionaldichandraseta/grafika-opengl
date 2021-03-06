#version 460 core
layout(location=0) in vec4 vPosition;
layout(location=1) in vec4 color;

out varying  vec4 normalColor;

void main()
{
    gl_Position = vPosition;
    normalColor = color;
}
import React, { useState, useEffect } from 'react';
import './App.css'; 

// Converts degrees to radians
const degToRad = (deg) => (deg * Math.PI) / 180;

// Clock hand component
const Hand = ({ angle, length, width, colorName, originX = 50, originY = 50 }) => {
  const x1 = originX;
  const y1 = originY;
  // Subtract 90 since for some reason svgs are tilted 90 degress clockwise
  const adjustedAngle = angle - 90;

  const x2 = originX + length * Math.cos(degToRad(adjustedAngle));
  const y2 = originY + length * Math.sin(degToRad(adjustedAngle));

  // Use a general hand class and specific class for color
  const handClasses = `hand ${colorName}`;

  return (
    <line
      x1={x1}
      y1={y1}
      x2={x2}
      y2={y2}
      className={handClasses}
      strokeWidth={width} 
      strokeLinecap="round"
    />
  );
};

// Main Analog Clock Component
const AnalogClock = () => {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timerId = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(timerId);
  }, []);

  // Calculations for the clock movements, not rly sure if this is the best way to do it
  const seconds = time.getSeconds();
  const secondsAngle = seconds * 6;

  const minutes = time.getMinutes();
  const minutesAngle = minutes * 6 + (seconds / 60) * 6;

  const hours = time.getHours();
  const hoursAngle = ((hours % 12) + minutes / 60) * 30;

  const clockSize = 500; // SVG viewBox size
  const center = clockSize / 2;
  const clockFaceRadius = clockSize / 2 - 2;

  // Create hour markers
  const hourMarkers = [];
  for (let i = 1; i <= 12; i++) {
    const angle = i * 30 - 90;
    const x1 = center + (clockFaceRadius - 15) * Math.cos(degToRad(angle));
    const y1 = center + (clockFaceRadius - 15) * Math.sin(degToRad(angle));
    const x2 = center + clockFaceRadius * Math.cos(degToRad(angle));
    const y2 = center + clockFaceRadius * Math.sin(degToRad(angle));
    hourMarkers.push(
      <line
        key={`hour-${i}`}
        x1={x1}
        y1={y1}
        x2={x2}
        y2={y2}
        className="hourMarker"
      />
    );
  }

  // Create minute markers
  const minuteMarkers = [];
  for (let i = 1; i <= 60; i++) {
    if (i % 5 !== 0) {
      const angle = i * 6 - 90;
      const x1 = center + (clockFaceRadius - 8) * Math.cos(degToRad(angle));
      const y1 = center + (clockFaceRadius - 8) * Math.sin(degToRad(angle));
      const x2 = center + clockFaceRadius * Math.cos(degToRad(angle));
      const y2 = center + clockFaceRadius * Math.sin(degToRad(angle));
      minuteMarkers.push(
        <line
          key={`minute-${i}`}
          x1={x1}
          y1={y1}
          x2={x2}
          y2={y2}
          className="minuteMarker"
        />
      );
    }
  }

  return (
    <div className="clockContainer">
      <svg
        width={clockSize}
        height={clockSize}
        viewBox={`0 0 ${clockSize} ${clockSize}`}
        className="clockSvg"
      >
        <circle
          cx={center}
          cy={center}
          r={clockFaceRadius}
          className="clockFace"
        />
        <circle cx={center} cy={center} r="7" className="centerDot" />

        {hourMarkers}
        {minuteMarkers}

        <Hand
          angle={hoursAngle}
          length={clockFaceRadius * 0.55}
          width="8"
          colorName="hourHandColor" 
          originX={center}
          originY={center}
        />
        <Hand
          angle={minutesAngle}
          length={clockFaceRadius * 0.8}
          width="6" 
          colorName="minuteHandColor" 
          originX={center}
          originY={center}
        />
        <Hand
          angle={secondsAngle}
          length={clockFaceRadius * 0.9}
          width="3" 
          colorName="secondHandColor" 
          originX={center}
          originY={center}
        />
      </svg>
    </div>
  );
};

// App component to render the clock
export default function App() {
  return (
    <div className="appContainer">
      <AnalogClock />
    </div>
  );
}

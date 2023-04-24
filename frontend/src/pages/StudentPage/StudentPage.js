import React from "react";
// import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
// import axios from "axios";

const StudentPage = () => {
  const [user, token] = useAuth();
  return (
    <div className="container">
      <h1>Student Page for {user.username}!</h1>
    </div>
  );
};

export default StudentPage;

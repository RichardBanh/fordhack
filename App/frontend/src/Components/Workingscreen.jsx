import React, { useState } from "react";

//auto save function?
export const WorkingScreen = () => {
  return (
    <>
      <div className="content">
        <div className="side_left">
          <div className="menubar">
            <div>Logo</div>
            <div className="accountType">Account Class: Admin</div>
            <div>Settings</div>
            <div>Security Console</div>
            <div>Log Out</div>
          </div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
        </div>
        <div className="side_right"></div>
      </div>
    </>
  );
};

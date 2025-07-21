// LightGalleryComponent.js
import React, { useEffect, useState } from 'react';
import lightGallery from 'lightgallery';

import lgZoom from 'lightgallery/plugins/zoom';
import lgThumbnail from 'lightgallery/plugins/thumbnail';

import 'lightgallery/css/lightgallery.css';
import 'lightgallery/css/lg-zoom.css';
import 'lightgallery/css/lg-thumbnail.css';

export function LightGalleryComponent({ images }) {
  const [selected, setSelected] = useState(images[0]);

    useEffect(() => {
    const gallery = document.getElementById("lightgallery-thumbs");
    let instance = null;
    if (gallery) {
        instance = lightGallery(gallery, {
        plugins: [lgZoom, lgThumbnail],
        speed: 500,
        download: false,
        });
    }

    return () => {
        if (instance) {
        instance.destroy();
        }
    };
    }, []);

  return (
    <div style={{ textAlign: "center" }}>
      {/* Imagen principal */}
      <img
        src={selected}
        alt="Selected"
        style={{
          maxWidth: "80%",
          borderRadius: "12px",
          marginBottom: "20px",
          transition: "all 0.3s ease-in-out",
          boxShadow: "0 8px 20px rgba(0,0,0,0.3)",
        }}
      />

      {/* Miniaturas con LightGallery */}
      <div
        id="lightgallery-thumbs"
          style={{
            display: "flex",
            flexDirection: "row",
            overflowX: "auto",
            gap: "10px",
            padding: "10px",
            scrollBehavior: "smooth",
            maxWidth: "100%",
        }}
      >
        {images.map((img, index) => (
          <a href={img} key={index}>
            <img
              src={img}
              style={{
                width: "80px",
                height: "auto",
                borderRadius: "6px",
                cursor: "pointer",
                border: img === selected ? "2px solid #0ea5e9" : "2px solid transparent",
                transition: "transform 0.2s ease-in-out",
              }}
              onClick={(e) => {
                e.preventDefault();
                setSelected(img);
              }}
              onMouseOver={(e) => (e.currentTarget.style.transform = "scale(1.05)")}
              onMouseOut={(e) => (e.currentTarget.style.transform = "scale(1)")}
            />
          </a>
        ))}
      </div>
    </div>
  );
}

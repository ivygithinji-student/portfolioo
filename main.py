from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Ivy Githinji - Backend Portfolio")

@app.get("/", response_class=HTMLResponse)
async def portfolio():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ivy Githinji - Backend Portfolio</title>
        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 40px;
                background: #faf8f6;
                color: #2d2d2d;
            }
            .container {
                max-width: 1000px;
                margin: 0 auto;
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 2px 20px rgba(0,0,0,0.06);
            }
            h1 {
                color: #2d2d2d;
                font-weight: 400;
                border-bottom: 3px solid #d4a0a0;
                padding-bottom: 12px;
            }
            .student-info {
                background: #fcf8f6;
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
                border-left: 4px solid #d4a0a0;
            }
            .student-info p {
                margin: 6px 0;
                font-size: 15px;
            }
            .student-info strong {
                color: #b87a7a;
            }
            .admission {
                color: #b87a7a;
                font-weight: 600;
            }
            .lab-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 14px;
                margin-top: 20px;
            }
            .lab-card {
                background: #fcf8f6;
                padding: 14px 18px;
                border-radius: 8px;
                border-left: 4px solid #d4a0a0;
                transition: all 0.2s ease;
            }
            .lab-card:hover {
                background: #f8f0ee;
                transform: translateX(4px);
            }
            .lab-card a {
                text-decoration: none;
                color: #2d2d2d;
                font-weight: 500;
                font-size: 14px;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .lab-card a:hover {
                color: #b87a7a;
            }
            .lab-card .badge {
                display: inline-block;
                background: #d4a0a0;
                color: white;
                padding: 2px 10px;
                border-radius: 12px;
                font-size: 11px;
                font-weight: 600;
            }
            .lab-card .badge-green {
                background: #b8a0a0;
            }
            .footer {
                margin-top: 30px;
                text-align: center;
                color: #b0a0a0;
                font-size: 13px;
                border-top: 1px solid #f0ecea;
                padding-top: 20px;
            }
            .instructions {
                background: #f8f4f2;
                padding: 14px 20px;
                border-radius: 8px;
                margin: 18px 0 22px 0;
                font-size: 14px;
                color: #5a4a4a;
                border-left: 4px solid #d4a0a0;
            }
            .instructions code {
                background: #f0ecea;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 13px;
                color: #b87a7a;
            }
            .lab-card .repo-name {
                font-weight: 300;
                color: #b0a0a0;
                font-size: 12px;
                margin-left: auto;
            }
            h2 {
                color: #2d2d2d;
                font-weight: 400;
                font-size: 1.2em;
                margin-bottom: 16px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Backend Development Portfolio</h1>
            
            <div class="student-info">
                <p><strong>Name:</strong> Ivy Githinji</p>
                <p><strong>Admission Number:</strong> <span class="admission">C027-01-0883/2024</span></p>
                <p><strong>Email:</strong> ivy.githinji24@students.dkut.ac.ke</p>
            </div>

            <div class="instructions">
                Click any lab below to view the complete code on GitHub. Each lab is a separate repository with full documentation.
            </div>

            <h2>Lab Assignments</h2>
            
            <div class="lab-grid">
                <div class="lab-card">
                    <span class="badge">Labs 1-4</span>
                    <a href="https://github.com/ivygithinji-student/gighub-api" target="_blank">
                        GigHub API
                        <span class="repo-name">GitHub</span>
                    </a>
                </div>
                
                <div class="lab-card">
                    <span class="badge">Labs 5-6</span>
                    <a href="https://github.com/ivygithinji-student/product-api" target="_blank">
                        Product API
                        <span class="repo-name">GitHub</span>
                    </a>
                </div>
                
                <div class="lab-card">
                    <span class="badge">Lab 7</span>
                    <a href="https://github.com/ivygithinji-student/healthtrack-api" target="_blank">
                        HealthTrack API
                        <span class="repo-name">GitHub</span>
                    </a>
                </div>
                
                <div class="lab-card">
                    <span class="badge">Lab 8</span>
                    <a href="https://github.com/ivygithinji-student/clinicguard-api" target="_blank">
                        ClinicGuard API
                        <span class="repo-name">GitHub</span>
                    </a>
                </div>
                
                <div class="lab-card">
                    <span class="badge">Lab 9</span>
                    <a href="https://github.com/ivygithinji-student/sendit-api" target="_blank">
                        SendIt API
                        <span class="repo-name">GitHub</span>
                    </a>
                </div>
                
                <div class="lab-card" style="border-left-color: #b8a0a0;">
                    <span class="badge badge-green">GitHub</span>
                    <a href="https://github.com/ivygithinji-student" target="_blank" style="color: #b87a7a;">
                        All Repositories
                        <span class="repo-name">Profile</span>
                    </a>
                </div>
            </div>

            <div class="footer">
                <p>Deployed on Render | Built with FastAPI | August 2026</p>
                <p style="font-size: 12px; color: #c0b0b0; margin-top: 4px;">
                    Ivy Githinji | C027-01-0883/2024
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

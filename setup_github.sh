#!/bin/bash

# AlfAI Core - GitHub Setup Script

echo "🚀 Setting up AlfAI Core on GitHub"
echo "=" * 50

# Initialize Git repository if not already done
if [ ! -d ".git" ]; then
    echo "🔧 Initializing Git repository..."
    git init
fi

# Add all files
echo "📦 Adding files to repository..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "AlfAI Core - Advanced AI Framework with 14-Layer Architecture

Features:
- 14-Layer Framework with Complete Processing Pipeline
- Sub-Modules: DRE (Data Reasoning), CMS (Content Management), EEI (Ethical Evaluation), CCE (Compliance Control)
- AXA-I → MFE → AlfAI Flow Integration
- Complete Flow Test: prompt → supervision → reasoning → audit
- RESTful API with 8 Endpoints
- FastAPI Backend with Comprehensive Documentation
- Ethical Evaluation (8 Principles)
- Compliance Checking (8 Standards: GDPR, CCPA, HIPAA, SOX, PCI-DSS, ISO27001, NIST, ADA)
- Advanced Data Reasoning and Pattern Recognition
- Content Management and Quality Assessment
- Production-Ready Deployment

Architecture:
- 14-Layer Processing Pipeline
- Sub-Module Integration (DRE, CMS, EEI, CCE)
- Flow Management (AXA-I, MFE, AlfAI)
- RESTful API with FastAPI
- Comprehensive Testing and Validation
- Complete Documentation and API Map

Ready for production deployment!"

echo "✅ AlfAI Core repository prepared"
echo ""
echo "🌐 To create GitHub repository:"
echo "1. Go to https://github.com/new"
echo "2. Repository name: alfai-core"
echo "3. Description: Advanced AI Framework with 14-Layer Architecture, DRE, CMS, EEI, and CCE Modules"
echo "4. Make it public"
echo "5. Don't initialize with README"
echo ""
echo "Then run:"
echo "git remote add origin https://github.com/YOUR_USERNAME/alfai-core.git"
echo "git branch -M main"
echo "git push -u origin main"
echo ""
echo "Repository will be available at: https://github.com/YOUR_USERNAME/alfai-core"

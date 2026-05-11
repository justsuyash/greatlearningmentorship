import re

with open('templates/index.html', 'r') as f:
    content = f.read()

# HTML & Body
content = content.replace('<html lang="en">', '<html lang="en" data-theme="corporate">')
content = content.replace('<body>', '<body class="bg-base-100 text-base-content h-screen flex flex-col m-0 p-0 font-sans">')

# Pyodide loader
content = content.replace('<div id="pyodide-loader">', '<div id="pyodide-loader" class="fixed top-4 right-8 bg-warning text-warning-content px-4 py-2 rounded-md font-semibold z-50">')

# Navbar
content = content.replace('<div class="navbar">', '<div class="navbar bg-base-100 border-b border-base-200 px-8 min-h-[56px] flex justify-between items-center box-border">')
content = content.replace('<div class="tabs">', '<div class="flex gap-4">')
content = content.replace('class="tab-btn active"', 'class="tab-btn active pb-2 px-5 text-base font-semibold text-blue-600 border-b-2 border-blue-600 cursor-pointer"')
content = content.replace('class="tab-btn"', 'class="tab-btn pb-2 px-5 text-base font-semibold text-gray-400 border-b-2 border-transparent hover:text-gray-600 cursor-pointer"')

# Layout
content = content.replace('<div class="app-layout">', '<div class="flex flex-1 overflow-hidden">')
content = content.replace('<div class="global-sidebar">', '<div class="w-64 bg-base-100 border-r border-base-200 p-4 overflow-y-auto">')
content = content.replace('<div class="content-area">', '<div class="flex-1 p-8 overflow-y-auto">')

# Cards
content = content.replace('class="card"', 'class="card bg-base-100 shadow-sm border border-base-200 p-8 mb-6"')
content = content.replace('class="card" style="padding:32px;"', 'class="card bg-base-100 shadow-sm border border-base-200 p-8 mb-6"')
content = content.replace('class="card" style="display:none; overflow-x:auto;"', 'class="card bg-base-100 shadow-sm border border-base-200 p-8 mb-6" style="display:none; overflow-x:auto;"')

# Buttons
content = content.replace('class="btn"', 'class="btn btn-primary"')
content = content.replace('class="btn btn-full"', 'class="btn btn-primary w-full mt-6"')

# Tables
content = content.replace('table style="width:100%; border-collapse:collapse; margin-bottom:32px; text-align:left;"', 'table class="table table-zebra w-full mb-8"')
content = content.replace('table style="width:100%; border-collapse:collapse; text-align:left;"', 'table class="table table-zebra w-full"')
content = content.replace('<table style="width:100%; font-size:14px;">', '<table class="table table-xs w-full">')

# Inline styles cleanup inside JS
content = content.replace('div.className = `sidebar-item ${id === activeExpId ? \'active\' : \'\'}`;', 'div.className = `px-3 py-2 cursor-pointer rounded-md mb-2 font-medium ${id === activeExpId ? \'bg-blue-50 text-blue-600\' : \'hover:bg-base-200\'}`;')

# JS Status Badges
content = content.replace('if(exp.status === "Planning") statusBadge.classList.add(\'planning\');\n        else if(exp.status === "Running") statusBadge.classList.add(\'running\');\n        else statusBadge.classList.add(\'decision\');', 'if(exp.status === "Planning") statusBadge.classList.add(\'badge-info\');\n        else if(exp.status === "Running") statusBadge.classList.add(\'badge-warning\');\n        else statusBadge.classList.add(\'badge-success\');')

# Fix checkboxes
content = content.replace('type="checkbox" ${checkedAttr} onchange="toggleChecklist(${idx})" style="margin-top:4px; cursor:pointer; width:16px; height:16px;"', 'type="checkbox" ${checkedAttr} onchange="toggleChecklist(${idx})" class="checkbox checkbox-success checkbox-sm mt-1"')

# Tab switching logic to handle tailwind classes
content = content.replace("document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));", "document.querySelectorAll('.tab-btn').forEach(el => { el.classList.remove('active'); el.className = 'tab-btn pb-2 px-5 text-base font-semibold text-gray-400 border-b-2 border-transparent hover:text-gray-600 cursor-pointer'; });")
content = content.replace("event.currentTarget.classList.add('active');", "event.currentTarget.className = 'tab-btn active pb-2 px-5 text-base font-semibold text-blue-600 border-b-2 border-blue-600 cursor-pointer';")

# Sidebar click logic
content = content.replace("document.querySelectorAll('.sidebar-item').forEach(el => el.classList.remove('active'));\n                e.target.classList.add('active');", "document.querySelectorAll('#globalSidebarExpList div').forEach(el => el.className = 'px-3 py-2 cursor-pointer rounded-md mb-2 font-medium hover:bg-base-200');\n                e.target.className = 'px-3 py-2 cursor-pointer rounded-md mb-2 font-medium bg-blue-50 text-blue-600';")

# Fix Pyodide Table Generation for nested MOCK_METRICS
pyodide_fix = """
df = pd.DataFrame(data).T.reset_index()
df = df.rename(columns={'index': 'variant'})
df['variant'] = df['variant'].str.capitalize()

# Calculate base metrics
df['Conversion Rate'] = df['conversions'] / df['sessions']
"""

old_pyodide = """
df = pd.DataFrame(data)

# Calculate base metrics
df['Conversion Rate'] = df['conversions'] / df['sessions']
"""

content = content.replace(old_pyodide, pyodide_fix)

# LangSmith Link
langsmith_link = """<div style="display:flex; justify-content:space-between; align-items:center;">
                    <h2>Executive Summary Generation</h2>
                    <div>
                        <a href="https://smith.langchain.com" target="_blank" class="btn btn-ghost btn-sm mr-2" title="View live agent traces in LangSmith">🔍 View in LangSmith</a>
                        <button class="btn btn-primary" id="runWorkflowBtn" onclick="runAgentWorkflow()">Create AI Summary</button>
                    </div>
                </div>"""

content = content.replace('<div style="display:flex; justify-content:space-between; align-items:center;">\n                    <h2>Executive Summary Generation</h2>\n                    <button class="btn btn-primary" id="runWorkflowBtn" onclick="runAgentWorkflow()">Create AI Summary</button>\n                </div>', langsmith_link)

with open('templates/index.html', 'w') as f:
    f.write(content)

print("Conversion script finished.")

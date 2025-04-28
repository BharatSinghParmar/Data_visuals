from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
import os

app = Flask(__name__)

# List of cities based on your data
cities = [
    "Visakhapatnam", "Itanagar", "Guwahati", "Patna", "Raipur", "Panaji", 
    "Ahmedabad", "Chandigarh", "Shimla", "Ranchi", "Bangalore", 
    "Thiruvananthapuram", "Bhopal", "Mumbai", "Imphal", "Shillong", 
    "Aizawl", "Kohima", "Bhubaneswar", "Amritsar", "Jaipur", 
    "Gangtok", "Chennai", "Hyderabad", "Agartala", "Lucknow", 
    "Dehradun", "Kolkata" , "Agra"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_city')
def select_city():
    return render_template('city_list.html', cities=cities)

@app.route('/plot_choice/<city>', methods=['GET', 'POST'])
def plot_choice(city):
    if request.method == 'POST':
        plot_type = request.form.get('plot_type')
        if plot_type == 'scatter':
            return redirect(url_for('show_scatter_plot', city=city))
        elif plot_type == 'line':
            return redirect(url_for('show_line_plot', city=city))
    return render_template('plot_choice.html', city=city)

@app.route('/scatter_plot/<city>')
def show_scatter_plot(city):
    filename = f'{city}_bokeh_plots.html'
    path = os.path.join('visuals_city_data', city)
    
    # Debugging statements
    print(f"Scatter Plot - Path: {path}, Filename: {filename}")
    full_path = os.path.join(path, filename)
    print(f"Full Path: {full_path}")
    
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        abort(404)  # Return a 404 error if file not found
    
    return send_from_directory(path, filename)

@app.route('/line_plot/<city>')
def show_line_plot(city):
    filename = f'{city}_bokeh_plots.html'
    path = os.path.join('bokeh_files', city)
    
    # Debugging statements
    print(f"Line Plot - Path: {path}, Filename: {filename}")
    full_path = os.path.join(path, filename)
    print(f"Full Path: {full_path}")
    
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        abort(404)  # Return a 404 error if file not found

    return send_from_directory(path, filename)

if __name__ == '__main__':
    app.run(debug=True)

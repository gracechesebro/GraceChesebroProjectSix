import dearpygui.dearpygui as dpg
import openpyxl
import comp151Colors
import Project5Helpers
#job data
jobs = Project5Helpers.get_job_data()
#Ask user input - salary 5 years after grad
desired_salary = int(input("Enter your desired salary for 5 years after graduation: "))
def scale_salary(amount):
    return amount // 500 #to fit bars
def draw_starting_salary_bars():
    x=70
    bar_width=20
    gap=35
    baseline = 700
    for job in jobs:
        title=job["job_class"]
        salary=job["starting_salary"]
        height = scale_salary(salary)
        top_y = baseline - height
        dpg.draw_rectangle((x, top_y), (x+ bar_width, baseline),
                           color=comp151Colors.WHITE, fill=comp151Colors.GREEN)
        dpg.draw_text((x+15, baseline+5), title, size=8)
        x+= gap

dpg.create_context()
dpg.create_viewport(title="Job Salaries Bar Graph",
                    width = 900, height=900)
with dpg.window(label="MA Tech Job Salaries Bar Graph", width=900, height=900):
    with dpg.drawlist(width=850, height=850):
        # X and Y axis
        dpg.draw_line((50, 100), (50, 700), color=comp151Colors.WHITE,
                      thickness=2)
        dpg.draw_line((50, 700), (800, 700), color=comp151Colors.WHITE,
                      thickness=2)

        draw_starting_salary_bars()
        baseline=700
        y = baseline - scale_salary(desired_salary)
        dpg.draw_line((50, y), (800, y), color=comp151Colors.YELLOW, thickness=2)
        dpg.draw_text((60, y-10), "Desired Salary", size=6, color=comp151Colors.YELLOW)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

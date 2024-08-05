import svgwrite
from svgwrite import cm, mm

def create_chart(title, checkpoints, current_stage, final_goal, key_requirements):
    dwg = svgwrite.Drawing('luxofy_chart.svg', size=(800, 600))
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='#f5f5f5'))
    
    # Header
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', 60), fill='url(#headerGradient)'))
    dwg.add(dwg.text(title, insert=(20, 40), fill='white', font_size='24px', font_weight="bold", font_family="Arial, sans-serif"))
    
    # Define gradient
    gradient = dwg.defs.add(dwg.linearGradient(id="headerGradient"))
    gradient.add_stop_color(0, '#1a237e')
    gradient.add_stop_color(100, '#283593')
    
    # Flow Chart
    checkpoint_width, checkpoint_height = 140, 70
    start_x, start_y = 50, 80
    max_per_row = 4
    for i, checkpoint in enumerate(checkpoints):
        x = start_x + (i % max_per_row) * (checkpoint_width + 40)
        y = start_y + (i // max_per_row) * (checkpoint_height + 50)
        color = '#2196F3'  # All checkpoints are blue by default
        rect = dwg.rect(insert=(x, y), size=(checkpoint_width, checkpoint_height), rx=5, ry=5, fill=color, stroke='#333', stroke_width=2)
        dwg.add(rect)
        lines = checkpoint.split()
        mid = len(lines) // 2
        dwg.add(dwg.text(lines[0], insert=(x + checkpoint_width/2, y + 30), fill='white', font_size='14px', text_anchor="middle", font_family="Arial, sans-serif"))
        dwg.add(dwg.text(' '.join(lines[1:]), insert=(x + checkpoint_width/2, y + 50), fill='white', font_size='14px', text_anchor="middle", font_family="Arial, sans-serif"))
        
        # Add green dot for current stage
        if checkpoint == current_stage:
            dwg.add(dwg.circle(center=(x + checkpoint_width - 10, y + 10), r=5, fill='#4CAF50'))
        
        # Add connecting lines
        if i < len(checkpoints) - 1:
            if (i + 1) % max_per_row != 0:
                dwg.add(dwg.line(start=(x + checkpoint_width, y + checkpoint_height/2),
                                 end=(x + checkpoint_width + 40, y + checkpoint_height/2),
                                 stroke='#333', stroke_width=2))
            else:
                dwg.add(dwg.line(start=(x + checkpoint_width/2, y + checkpoint_height),
                                 end=(x + checkpoint_width/2, y + checkpoint_height + 50),
                                 stroke='#333', stroke_width=2))
    
    # Final Goal
    goal_x = start_x + checkpoint_width * 1.5
    goal_y = start_y + ((len(checkpoints) - 1) // max_per_row + 1) * (checkpoint_height + 50)
    dwg.add(dwg.rect(insert=(goal_x, goal_y), size=(320, 80), rx=5, ry=5, fill='#9C27B0', stroke='#333', stroke_width=2))
    lines = final_goal.split()
    mid = len(lines) // 2
    dwg.add(dwg.text(' '.join(lines[:mid]), insert=(goal_x + 160, goal_y + 35), fill='white', font_size='16px', text_anchor="middle", font_family="Arial, sans-serif"))
    dwg.add(dwg.text(' '.join(lines[mid:]), insert=(goal_x + 160, goal_y + 60), fill='white', font_size='16px', text_anchor="middle", font_family="Arial, sans-serif"))
    
    # Connect last checkpoint to final goal
    last_x = start_x + ((len(checkpoints) - 1) % max_per_row) * (checkpoint_width + 40) + checkpoint_width/2
    last_y = start_y + ((len(checkpoints) - 1) // max_per_row) * (checkpoint_height + 50) + checkpoint_height
    dwg.add(dwg.line(start=(last_x, last_y), end=(goal_x + 160, goal_y), stroke='#333', stroke_width=2))
    
    # Key Requirements
    req_x, req_y = 550, 450
    dwg.add(dwg.rect(insert=(req_x, req_y), size=(230, 130), rx=5, ry=5, fill='white', stroke='#333', stroke_width=1))
    dwg.add(dwg.text('Key Requirements:', insert=(req_x + 10, req_y + 30), fill='#333', font_size='16px', font_weight="bold", font_family="Arial, sans-serif"))
    for i, req in enumerate(key_requirements):
        dwg.add(dwg.text(f'• {req}', insert=(req_x + 10, req_y + 60 + i*20), fill='#333', font_size='14px', font_family="Arial, sans-serif"))
    
    dwg.save()

def main():
    print("Welcome to the Montaigne Strategic Chart Generator!")
    title = input("Enter the chart title: ")
    checkpoints = []
    print("Enter checkpoints (one per line, leave blank to finish):")
    while True:
        checkpoint = input()
        if checkpoint == "":
            break
        checkpoints.append(checkpoint)
    
    current_stage = input("Enter the current stage (must match one of the checkpoints): ")
    while current_stage not in checkpoints:
        print("Error: Current stage must match one of the checkpoints.")
        current_stage = input("Enter the current stage (must match one of the checkpoints): ")
    
    final_goal = input("Enter the final goal: ")
    key_requirements = []
    print("Enter key requirements (one per line, leave blank to finish):")
    while True:
        requirement = input()
        if requirement == "":
            break
        key_requirements.append(requirement)
    
    create_chart(title, checkpoints, current_stage, final_goal, key_requirements)
    print("Chart has been generated as 'luxofy_chart.svg'")

if __name__ == "__main__":
    main()
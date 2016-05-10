from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_management_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def create(self, project):
        wd = self.app.wd
        self.open_project_management_page()
        # Init project creation
        wd.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td/form/input[2]").click()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None

    project_cache = None


    def select_project_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id=%s')]" % id).click()


    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_management_page()
        self.select_project_by_id(id)
        #submit deletion
        wd.find_element_by_xpath("/html/body/div[4]/form/input[3]").click()
        wd.find_element_by_xpath("/html/body/div[2]/form/input[4]").click()
        self.project_cache = None



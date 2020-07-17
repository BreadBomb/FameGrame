from datetime import datetime


class PropertyAnimation:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def get_value_by_percentage(self, percentage):
        part_full_percentage = 1 / (len(self.properties) - 1)
        current_index = int(percentage / part_full_percentage)
        part_percentage = (percentage - part_full_percentage * current_index) / part_full_percentage
        value = self.__get_part_value(current_index, part_percentage)
        return value

    def __get_part_value(self, index, percentage):
        if self.properties[index + 1] > self.properties[index]:
            return (self.properties[index + 1] - self.properties[index]) * percentage
        else:
            return self.properties[index] - (self.properties[index] -
                                             self.properties[index + 1]) * percentage


class ValueAnimation:
    def __init__(self, obj, properties, duration, round_values=True, loop=True):
        """
        @param obj: The object witch parameters should be animated
        @param properties: The properties (Format: {x=[0, 100]})
        """
        self.object = obj
        self.propertie_animations = self.__create_property_animations(properties)
        self.duration = duration / 1000
        self.round_values = round_values
        self.loop = loop

        self.start_time = None

    def __create_property_animations(self, properties):
        property_animations = []

        for key in properties:
            property_animations.append(PropertyAnimation(key, properties[key]))

        return property_animations

    def run(self):
        if self.start_time is None:
            self.start_time = datetime.now().timestamp()
        time = datetime.now().timestamp()

        percentage = (time - self.start_time) / self.duration

        if percentage > 1 and self.loop:
            self.start_time = datetime.now().timestamp()
            percentage = 0.0
        elif percentage > 1 and not self.loop:
            return self.object

        for animation in self.propertie_animations:
            value = animation.get_value_by_percentage(percentage)
            if self.round_values:
                value = round(value)
            setattr(self.object, animation.name, value)

        return self.object

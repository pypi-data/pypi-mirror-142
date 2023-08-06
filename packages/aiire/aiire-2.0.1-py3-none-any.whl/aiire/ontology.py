"""
This module provides the ontology functionality.

It defines the `Ontology' class, as well as `Ontology.Concept'.
These classes are intended to be subclassed in applications.
"""

from typing import Iterable


class Ontology(object):
    """
    `Ontology' is the base class of ontologies.

    An Ontology instance contain concepts (Concept instances).
    It can retrieve concepts by their unique names or ids.

    @ivar by_name: a mapping from names to concepts
    """

    def __init__(self):
        """Construct an Ontology instance."""
        self.by_name = {}

    def create_or_get(self, name: str):
        """
        Create a new concept or retrieve it by name.

        If the ontology has a concept with such name, then
        this concept is returned.
        Otherwise, a new concept is created, stored in the
        ontology, and returned.

        @param name: the name of the concept
        @return: the concept (retrieved or created)
        """
        if name in self.by_name:
            return self.by_name[name]
        conc = self.Concept(name, self)
        self.by_name[name] = conc
        return conc

    def create_group(
        self,
        items: Iterable['Concept'],
        conc_name: str = 'group',
        rel_name: str = 'include',
        inh_name: str = 'inheritance'
    ):
        """
        Create a concept of a group of concepts from given items.

        @param items: a collection of items to be added to the group
        @param conc_name: the group concept name in the ontology
        @param rel_name: the ontology name of the relation between
            group concept and its items
        @param inh_name: inheritance relation name in the ontology
        """
        groupcls = self.create_or_get(conc_name)
        include = self.create_or_get(rel_name)
        group = self.Concept(conc_name, self)
        inheritance = self.create_or_get(inh_name)
        group.add_attr(inheritance, groupcls)
        for item in items:
            group.add_attr(include, item)
        return group

    class Concept(object):
        """
        `Concept' is the base class for concepts.

        Concepts have attributes, i.e. are subjects of relations to
        other concepts.
        Concept always belongs to a certain ontology.

        @ivar name: the name of the concept
        @ivar ontology: the ontology to which the concept belongs
        @ivar attrs: concept's attributes relation->object mapping
        @ivar id: an integer identifier of the concept
        """

        _last_id = 0

        def __init__(self, name: str, ontology: 'Ontology'):
            """
            Construct a Concept instance.

            @param name: the name of the concept
            @param ontology: the ontology of the concept
            """
            self.name = name
            self.ontology = ontology
            self.attrs = {}
            self.id = self._last_id + 1
            self.__class__._last_id = self.id

        def add_attr(
            self,
            reltype: 'Ontology.Concept',
            obj: 'Ontology.Concept'
        ):
            """
            Add a new attribute to the concept.

            @param reltype: relation type concept
            @param obj: relation object concept
            """
            self.attrs.setdefault(reltype, []).append(obj)

        def getattr(self, attrname) -> Iterable['Ontology.Concept']:
            """
            Get attribute by relation name.

            @param attrname: the name of the relation
            @return: objects of this relation
            """
            return self.attrs[self.ontology.create_or_get(attrname)]

        def __str__(self) -> str:
            """
            Make a string representation of the concept.

            @return representation
            """
            return f'{self.name}:\n    ' + (
                '\n    '.join(
                    f'{attr.name}: '
                    '{", ".join(c.name for c in self.attrs[attr])}'
                    for attr in self.attrs
                )
            )

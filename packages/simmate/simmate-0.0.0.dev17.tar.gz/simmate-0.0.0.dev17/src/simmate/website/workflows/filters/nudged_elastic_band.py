# -*- coding: utf-8 -*-

from django_filters import rest_framework as filters

from simmate.website.workflows.filters import Structure
from simmate.database.base_data_types.nudged_elastic_band import (
    DiffusionAnalysis as DiffusionAnalysisTable,
    MigrationHop as MigrationHopTable,
    MigrationImage as MigrationImageTable,
)


class DiffusionAnalysis(Structure):
    class Meta:
        model = DiffusionAnalysisTable
        fields = dict(
            migrating_specie=["exact"],
            vacancy_mode=["exact"],
            atomic_fraction=["exact", "range"],
            barrier_cell=["range"],
            npaths_involved=["exact", "range"],
            **Structure.get_fields()
        )


class MigrationHop(filters.FilterSet):
    class Meta:
        model = MigrationHopTable
        fields = dict(
            site_start=["exact", "range"],
            site_end=["exact", "range"],
            number=["exact", "range"],
            length=["exact", "range"],
            dimension_path=["exact", "range"],
            dimension_host_lattice=["exact", "range"],
            energy_barrier=["exact", "range"],
        )


class MigrationImage(Structure):
    class Meta:
        model = MigrationImageTable
        fields = dict(
            number=["exact"],
            force_tangent=["range"],
            energy=["range"],
            structure_distance=["range"],
            **Structure.get_fields()
        )

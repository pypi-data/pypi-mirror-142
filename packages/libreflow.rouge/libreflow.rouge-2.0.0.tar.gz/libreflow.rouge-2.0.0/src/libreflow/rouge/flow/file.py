import pathlib

from libreflow.baseflow.file import (
    SyncStatutes           as BaseSyncStatutes,
    Revision               as BaseRevision,
    TrackedFolderRevision  as BaseTrackedFolderRevision,
    Revisions              as BaseRevisions,
    TrackedFolderRevisions as BaseTrackedFolderRevisions,
    HistorySyncStatutes    as BaseHistorySyncStatutes,
    TrackedFile            as BaseTrackedFile,
    FileSystemMap          as BaseFileSystemMap
)
from libreflow.utils.flow import get_contextual_dict, get_context_value


class SyncStatutes(BaseSyncStatutes):

    def collection_name(self):
        return self.root().project().get_entity_manager().sync_statutes.collection_name()


class Revision(BaseRevision):

    def get_default_path(self):
        path_format = get_contextual_dict(self, 'settings').get(
            'path_format', None
        )
        if path_format is None:
            path = super(Revision, self).get_default_path()
        else:
            path = self._compute_path(path_format)
        
        return path

    def compute_child_value(self, child_value):
        if child_value is self.file_name:
            self.file_name.set('{filename}_{revision}.{ext}'.format(
                filename=self._file.complete_name.get(),
                revision=self.name(),
                ext=self._file.format.get(),
            ))
        else:
            super(Revision, self).compute_child_value(child_value)


class TrackedFolderRevision(BaseTrackedFolderRevision):

    def get_default_path(self):
        path_format = get_contextual_dict(self, 'settings').get(
            'path_format', None
        )
        if path_format is None:
            path = super(Revision, self).get_default_path()
        else:
            path = self._compute_path(path_format)
        
        return path

    def compute_child_value(self, child_value):
        if child_value is self.file_name:
            self.file_name.set('{filename}_{revision}'.format(
                filename=self._file.complete_name.get(),
                revision=self.name()
            ))
        else:
            super(TrackedFolderRevision, self).compute_child_value(child_value)


class Revisions(BaseRevisions):

    def collection_name(self):
        return self.root().project().get_entity_manager().revisions.collection_name()


class TrackedFolderRevisions(BaseTrackedFolderRevisions):

    @classmethod
    def mapped_type(cls):
        return TrackedFolderRevision
    
    def collection_name(self):
        return self.root().project().get_entity_manager().revisions.collection_name()


class HistorySyncStatutes(BaseHistorySyncStatutes):
    
    def collection_name(self):
        return self.root().project().get_entity_manager().sync_statutes.collection_name()


class FileSystemMap(BaseFileSystemMap):
    
    def get_parent_path(self):
        file_path = get_context_value(self, 'file_path', delim='/')
        
        if file_path is None:
            file_path = ''
        
        return file_path

    def revision_collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.revisions.collection_name()
    
    def statutes_collection_name(self):
        return self.root().project().get_entity_manager().sync_statutes.collection_name()

    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.files.collection_name()

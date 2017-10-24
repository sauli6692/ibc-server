import { BaseSequelizeService, ISchema } from '../../../core/domain/services';
import { Collaborator } from './collaborator.model';

export class CollaboratorService extends BaseSequelizeService {
    protected define() {
        return {
            route: 'collaborators',
            model: Collaborator
        };
    }

    protected defineCreateSchema(): ISchema {
        return {};
    }

    protected defineUpdateSchema(): ISchema {
        return {};
    }
}

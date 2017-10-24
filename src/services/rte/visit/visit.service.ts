import { BaseSequelizeService, ISchema } from '../../../core/domain/services';
import { Visit } from './visit.model';

export class VisitService extends BaseSequelizeService {
    protected define() {
        return {
            route: 'visits',
            model: Visit
        };
    }

    protected defineCreateSchema(): ISchema {
        return {};
    }

    protected defineUpdateSchema(): ISchema {
        return {};
    }
}

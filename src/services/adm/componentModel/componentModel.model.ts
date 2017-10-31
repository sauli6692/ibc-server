// See http://docs.sequelizejs.com/en/latest/docs/models-definition/
// for more of what you can do here.
const Sequelize = require('sequelize');
import { BaseModel, IAssociation } from '../../../core/domain/models';
import { logger } from '../../../core/utils/logger';

export class ComponentModel extends BaseModel {
	protected define() {
		return {
			name: 'ComponentModel',
			fields: {
				componentId: {
					type: Sequelize.INTEGER,
					primaryKey: true
				},
				modelId: {
                    type: Sequelize.INTEGER,
					primaryKey: true
				},
				privileges: {
					type: Sequelize.STRING(4),
					allowNull: false
				}
			}
		};
	}
}

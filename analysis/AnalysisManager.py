# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Analysis manager
# -----------------------------------------------------------------------

import MotionAnalysisManager
import QuestionnaireAnalysisManager

if __name__ in '__main__':

	# Questionnaire
	# # Export
	questionnaireAnalysisExport = QuestionnaireAnalysisManager.QUESTIONNAIRE_Export('AllQuestionnaireData_20220202.xlsx')
	# # Analysis
	questionnaireAnalysis = QuestionnaireAnalysisManager.QUESTIONNAIRE_Analysis('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Analysis/ExData/Questionnaire/CutData/AllQuestionnaireData_20220202.xlsx')

	motionAnalysis = MotionAnalysisManager.MOTIONAN_ALYSIS()
	motionAnalysis.main()

	print('--- finish --- : AnalysisManager')
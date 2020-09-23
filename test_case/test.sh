set -o errexit
set -o pipefail
set -o nounset
set -o errtrace

readonly TMPDIR=$(dirname $(mktemp -u))
readonly SCRIPT_DIR=$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd );

python ${SCRIPT_DIR}/../exercice.py < ${SCRIPT_DIR}/test.1.input > ${TMPDIR}/test.1.tmp
diff ${TMPDIR}/test.1.tmp ${SCRIPT_DIR}/test.1.output

python ${SCRIPT_DIR}/../exercice.py < ${SCRIPT_DIR}/test.2.input > ${TMPDIR}/test.2.tmp
diff ${TMPDIR}/test.2.tmp ${SCRIPT_DIR}/test.2.output

echo "TEST OK"

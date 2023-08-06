import { faAngleDoubleLeft, faAngleDoubleRight, faAngleLeft, faAngleRight, } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Button, NumberField, Option, Select, } from '@jupyter-notebook/react-components';
import { InlineLoader } from '@quetz-frontend/apputils';
import * as React from 'react';
export const Pagination = ({ pageSize, pageCount, gotoPage, canPreviousPage, previousPage, nextPage, canNextPage, pageIndex, pageOptions, setPageSize, loading, }) => (React.createElement("div", { className: "jp-table-controls" },
    React.createElement("div", { className: "jp-table-controls-left" },
        React.createElement("div", { className: "btn-group" },
            React.createElement(Button, { title: "Go to first page", appearance: "stealth", onClick: () => gotoPage(0), disabled: !canPreviousPage },
                React.createElement(FontAwesomeIcon, { icon: faAngleDoubleLeft })),
            React.createElement(Button, { title: "Go to previous page", appearance: "stealth", onClick: () => previousPage(), disabled: !canPreviousPage },
                React.createElement(FontAwesomeIcon, { icon: faAngleLeft })),
            React.createElement(Button, { title: "Go to next page", appearance: "stealth", onClick: () => nextPage(), disabled: !canNextPage },
                React.createElement(FontAwesomeIcon, { icon: faAngleRight })),
            React.createElement(Button, { title: "Go to last page", appearance: "stealth", onClick: () => gotoPage(pageCount - 1), disabled: !canNextPage },
                React.createElement(FontAwesomeIcon, { icon: faAngleDoubleRight }))),
        React.createElement("div", { className: "jp-table-controls-text" }, loading ? (React.createElement(InlineLoader, null)) : (React.createElement("p", { className: "paragraph padding-text" },
            "Page",
            ' ',
            React.createElement("strong", null,
                pageIndex + 1,
                " of ",
                pageOptions.length))))),
    React.createElement("div", { className: "jp-table-controls-right jp-table-controls-text" },
        React.createElement("p", { className: "paragraph padding-side" },
            "Go to page: \u2003",
            React.createElement(NumberField, { value: pageIndex + 1, onChange: (e) => {
                    // @ts-expect-error target has value
                    const page = e.target.value ? Number(e.target.value) - 1 : 0;
                    gotoPage(page);
                }, style: { width: '100px' } })),
        React.createElement("p", { className: "paragraph padding-side" },
            React.createElement(Select, { value: pageSize, onChange: (e) => {
                    // @ts-expect-error target has value
                    setPageSize(Number(e.target.value));
                } }, [25, 50, 100].map((pageSize) => (React.createElement(Option, { key: pageSize, value: pageSize.toString(), defaultValue: "25" },
                "Show ",
                pageSize))))))));
//# sourceMappingURL=pagination.js.map